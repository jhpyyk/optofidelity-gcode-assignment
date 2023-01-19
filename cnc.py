import MachineClient
import sys

def main(args):
    file_path = "./{}".format(args[1])
    if (file_path[-6:] != '.gcode'):
        print("Invalid argument: not a gcode file")
        return

    lines = parse_lines(file_path)
    print(lines)

def parse_lines(file_path):
    """ 
    Parses lines from a G-Code file.

    Args:
    gcode_file: 
    """

    gcode_file = open(file_path)
    lines = []

    while True:
        line = gcode_file.readline()

        if not line:
            break
        
        if (line[0] == 'N'):
            line = line.strip()
            line = line.strip('\n')
            lines.append(line.split(" "))
    
    return lines


if __name__ == "__main__":
    main(sys.argv)