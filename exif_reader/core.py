from PIL import Image
from PIL.ExifTags import TAGS


def read_exif_data(image):
    return {
        TAGS[k]: v
        for k, v in image._getexif().items()
        if k in TAGS
    }


def read_image(path):
    return Image.open(path)
