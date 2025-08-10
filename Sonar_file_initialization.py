####################################################################################
############### Initialize acoustic metadata ###########
####################################################################################
import os
import cv2
import pyARIS # PyARIS: Python interface for ARIS sonar data processing
              # Source: https://github.com/EminentCodfish/pyARIS
              # Please cite the repository when using this package in research.


def process_aris_file(file_path: str, output_dir: str, frame_interval: int = 1) -> None:
    """
    Process a single ARIS (.aris) file and extract frames at specified intervals.

    Args:
        file_path (str): Path to the ARIS file.
        output_dir (str): Directory to save extracted sonar frames.
        frame_interval (int): Interval between frames to save. Default is 1 (save all).
    """
    try:
        # Load ARIS acoustic data
        aris_data = pyARIS.DataImport(file_path)
        total_frames = aris_data.FrameCount

        # Create output subdirectory named after the file (without extension)
        file_stem = os.path.splitext(os.path.basename(file_path))[0]
        frame_folder = os.path.join(output_dir, file_stem)
        os.makedirs(frame_folder, exist_ok=True)

        # Extract and save sonar frames
        for i in range(0, total_frames, frame_interval):
            frame = pyARIS.FrameRead(aris_data, i)
            frame_filename = os.path.join(frame_folder, f"frame_{i}.jpg")
            cv2.imwrite(frame_filename, frame.remap)

        print(f"[INFO] Processed {file_stem}: {total_frames} frames, saved every {frame_interval} frame(s).")
    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {e}")
    finally:
        cv2.destroyAllWindows()


def process_directory(dir_path: str, frame_interval: int = 1) -> None:
    """
    Process all (*.aris) files in a given directory.

    Args:
        dir_path (str): Directory containing .aris files.
        frame_interval (int): Interval between sonar frames to save.
    """
    for filename in os.listdir(dir_path):
        if filename.lower().endswith(".aris"):
            file_path = os.path.join(dir_path, filename)
            process_aris_file(file_path, dir_path, frame_interval)


def process_root_directory(root_path: str, frame_interval: int = 1) -> None:
    """
    Recursively process all subdirectories under a root directory for ARIS data extraction.

    Args:
        root_path (str): Root directory containing multiple subdirectories with .aris files.
        frame_interval (int): Interval between sonar frames to save.
    """
    for entry in os.listdir(root_path):
        subdir_path = os.path.join(root_path, entry)
        if os.path.isdir(subdir_path):
            process_directory(subdir_path, frame_interval)

if __name__ == "__main__":
    # ------------------- Configuration ------------------- #
    # Set root directory where ARIS subfolders are stored
    root_directory: str = "/path/to/ARIS/data"  # <-- Update this path

    # Set frame extraction interval (e.g., 10 = every 10 frames)
    frame_interval: int = 10  # <-- Customize as needed

    # ------------------- Start Processing ------------------- #
    if not os.path.exists(root_directory):
        print(f"[ERROR] Root directory does not exist: {root_directory}")
    else:
        process_root_directory(root_directory, frame_interval)
