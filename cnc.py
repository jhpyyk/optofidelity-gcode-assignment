import sys

import MachineClient
import Parser

def main(args):
    parser = Parser.Parser()
    commands = parser.parse_file(args[1])
    print(commands)

if __name__ == "__main__":
    main(sys.argv)