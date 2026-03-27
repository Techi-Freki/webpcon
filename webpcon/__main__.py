from .converter import Converter, Format
from .cli import CLI


if __name__ != '__main__':
    pass

def main():
    cli = CLI()
    Converter.convert(cli.args.input_file, cli.args.output_file, Format[cli.args.format])

main()
