from .converter import Converter
from .cli import CLI


if __name__ != "__main__":
    pass

def main():
    cli = CLI()
    Converter.convert(cli.args.input_file, cli.args.output_file, cli.args.format)

main()
