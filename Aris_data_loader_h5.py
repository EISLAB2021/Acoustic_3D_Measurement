import click
import ctypes
import os
from file_header import ArisFileHeader
from frame_header import ArisFrameHeader
import numpy as np
import h5py


class ArisFileLoader:
    """
    A class to load and parse ARIS sonar data files (.aris),
    and convert them into HDF5 (.h5) format for structured access.
    """

    def __init__(self, file_path):
        """
        Initialize the loader with the given file path.

        Args:
            file_path (str): Path to the .aris file
        """
        self.file_path = file_path
        self.header = None

    def validate(self):
        """
        Validate the ARIS file by reading and checking its file header.

        Returns:
            ArisFileHeader or None: Parsed header object or None if validation fails
        """
        try:
            click.echo(f"Reading file header from {self.file_path}...")
            with open(self.file_path, "rb") as file:
                data = file.read(1024)
                self.header = ArisFileHeader()
                ctypes.memmove(ctypes.addressof(self.header), data, ctypes.sizeof(self.header))

            click.echo("[✓] File header read successfully.")
        except FileNotFoundError:
            click.echo(f"Error: File not found at {self.file_path}")
            return None

        except Exception as e:
            click.echo(f"Error reading file header: {e}")
            return None

        # Sanity check: confirm header version
        if self.header.Version == 0x05464444:
            click.echo("[✓] Sanity check passed.")
        else:
            click.echo("[✗] Sanity check failed.")
            self.header = None
            return None

        # Display header information
        click.echo("File Header Information:")
        click.echo(f"-  FrameCount: {self.header.FrameCount}")
        click.echo(f"-  NumRawBeams: {self.header.NumRawBeams}")
        click.echo(f"-  SampleRate: {self.header.SampleRate}")
        click.echo(f"-  SamplesPerChannel: {self.header.SamplesPerChannel}")

        return self.header

    def parse_to_h5(self, output_path):
        """
        Parse the ARIS file into HDF5 format.

        Args:
            output_path (str): Path to save the converted .h5 file
        """
        self.validate()
        if self.header is None:
            click.echo("Error: File header not found.")
            return None

        file = None
        h5file = None

        try:
            # Create HDF5 file
            h5file = h5py.File(output_path, "w")

            # Save file header attributes into a group
            header_group = h5file.create_group("file_header")
            for field in self.header._fields_:
                header_group.attrs[field[0]] = getattr(self.header, field[0])

            file = open(self.file_path, "rb")
            file.seek(1024)  # Skip past the file header

            count = 0
            while True:
                # Read frame header
                frame_header = ArisFrameHeader()
                header_data = file.read(ctypes.sizeof(frame_header))
                if not header_data:
                    break
                ctypes.memmove(ctypes.addressof(frame_header), header_data, ctypes.sizeof(frame_header))

                col = int(frame_header.get_beams_from_pingmode())
                row = int(frame_header.SamplesPerBeam)

                # Validate frame version
                if frame_header.Version != 0x05464444:
                    click.echo(f"[✗] {frame_header.FrameIndex} frame header is invalid, skipping...")
                    file.seek(row * col, 1)
                    continue

                # Read and reshape frame data
                frame_data = file.read(row * col)
                frame_array = np.frombuffer(frame_data, dtype=np.uint8).reshape((row, col))

                # Save frame header and data to HDF5
                frame_group = h5file.create_group(f"frame_{frame_header.FrameIndex}")
                for field in frame_header._fields_:
                    frame_group.attrs[field[0]] = getattr(frame_header, field[0])
                frame_group.create_dataset("frame_data", data=frame_array, compression="gzip")

                count += 1
                click.echo(
                    f"[✓] Frame {frame_header.FrameIndex} read. "
                    f"Min = {np.min(frame_array)}, Max = {np.max(frame_array)}, Shape = {frame_array.shape}"
                )

            click.echo(f"{count}/{self.header.FrameCount} frames read successfully.")
        except FileNotFoundError:
            click.echo(f"Error: File not found at {self.file_path}")
        except Exception as e:
            click.echo(f"Error parsing file: {e}")
        finally:
            if file:
                file.close()
            if h5file:
                h5file.close()


@click.command()
@click.option("--input_folder", help="Path to the input folder containing .aris files", required=True)
@click.option("--output_folder", help="Path to the output folder to save .h5 files", required=True)
def main(input_folder, output_folder):
    """
    Command-line interface to batch-convert ARIS files in a folder to HDF5 format.
    """
    aris_files = [f for f in os.listdir(input_folder) if f.endswith('.aris')]

    for aris_file in aris_files:
        input_file = os.path.join(input_folder, aris_file)
        output_file = os.path.join(output_folder, os.path.splitext(aris_file)[0] + ".h5")

        click.echo(f"Processing file: {input_file}")
        loader = ArisFileLoader(input_file)
        loader.parse_to_h5(output_file)


if __name__ == "__main__":
    main()
