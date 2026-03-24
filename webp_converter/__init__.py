from PIL import Image
import os


class Converter(object):
    @staticmethod
    def convert(input_file: str, output_file: str):
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{input_file} does not exist.")

        try:

            with Image.open(input_file) as img:
                if img.mode == "CMYK":
                    img.convert("RGB")

                img.save(output_file, "PNG", quality=85)
                print(f"File successfully converted, file saved to {output_file}")
        except (IOError) as e:
            print(f"Error converting file {e}")
