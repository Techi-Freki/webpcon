import os

from enum import Enum, unique
from PIL import Image


@unique
class Format(Enum):
    JPEG = 0
    PNG = 1

class Converter(object):
    @staticmethod
    def convert(input_file:str, output_file:str, file_format:Format=Format.PNG):
        err = 'Error converting the image: {}'
        if not os.path.exists(input_file):
            no_file = f'{input_file} does not exist.'
            print(err.format(no_file))
            raise FileNotFoundError(err.format(no_file))

        try:

            with Image.open(input_file) as img:
                if img.mode == 'CMYK':
                    img.convert('RGB')

                img.save(output_file, file_format.name, quality=85)
                print(f'File successfully converted, file saved to {output_file}.')
        except Exception as e:
            print(err.format(e) + '.')
            raise IOError(e)
