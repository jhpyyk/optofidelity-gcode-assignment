import MachineClient
import sys

def main(args):
    file_path = "./{}".format(args[1])
    if (file_path[-6:] != '.gcode'):
        print("Invalid argument: not a gcode file")
        return

    lines = parse_file(file_path)
    
    

def parse_file(file_path):
    """ 
    Parses lines from a G-Code file.

    Args:
    file_path (string): Path to the G-code file.

    Returns:
    lines (array): Array of all the lines. Each line is split into strings with
                   space being the separator.
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