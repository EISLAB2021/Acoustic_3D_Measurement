import click
from Aris_data_loader_h5 import ArisFileLoader


@click.command()
@click.argument("file_path")
def validate(file_path):
    loader = ArisFileLoader(file_path)
    loader.validate()


@click.command()
@click.argument("file_path")
@click.argument("output_path")
def parse_to_h5(file_path, output_path):
    loader = ArisFileLoader(file_path)
    loader.parse_to_h5(output_path)
