import argparse
import json
import sys

from exif_reader.core import read_exif_data, read_image
from exif_reader.json_encoder import BytesEncoder


parser = argparse.ArgumentParser(description='Read EXIF data from a JPG')
parser.add_argument(
    'file_names',
    metavar='File Name',
    nargs='+',
    help='File names whose EXIF data to read',
)


def main():
    args = parser.parse_args()
    data = [
        read_exif_data(read_image(file_name))
        for file_name in args.file_names
    ]
    json.dump(data, sys.stdout, indent=4, cls=BytesEncoder)
