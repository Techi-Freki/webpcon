import argparse
from enum import Enum, unique


class CLI(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                prog="webpcon",
                description="Converts webp files to either JPG or PNG.",
                epilog="Copyright © Techi-Freki")
        self._load_args()
        self.args = self.parser.parse_args()

    def _load_args(self):
        self.parser.add_argument("input_file", help="the webp to convert.")
        self.parser.add_argument("output_file", help="The file to be outputted.")
        self.parser.add_argument("-f", "--format", choices=["PNG", "JPG"], default="PNG", help="The format to convert to [PNG, JPG], defaults to PNG.")
