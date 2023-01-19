class Parser():
    def __init__(self):
        self.last_x = 0.0
        self.last_y = 0.0
        self.last_z = 0.0

    def parse_file(self, file_path):
        if (file_path[-6:] != '.gcode'):
            print("Invalid argument: not a gcode file")
            return

        lines = self.parse_file_to_lines(file_path)
        commands = self.parse_lines_to_commands(lines)
        
        return commands
    
    

    def parse_file_to_lines(self, file_path):
        """ 
        Parses lines from a G-Code file.

        Args:
        file_path (string): Path to the G-code file.

        Returns:
        lines (array): Array of all the lines. Each line is split into strings with
                    space being the separator.
        """

        gcode_file = open(file_path)
        line_arr = []

        while True:
            line = gcode_file.readline()

            if not line:
                break
            
            if (line[0] == 'N'):
                line = line.strip()
                line = line.strip('\n')
                line_arr.append(line.split(" "))

        gcode_file.close()
        
        return line_arr

    def parse_lines_to_commands(self, lines):
        """
        Parses commands from an array of parsed G-Code lines.

        Args:
        lines (array): Array of parsed G-Code lines.

        Returns:
        commands (array): Array of commands.
        """

        command_arr = []
        command_buffer = []
        coordinate_args = {'X', 'Y', 'Z'}

        for line in lines:
            line_number = line[0]
            line = line[1:]
            for code in line:
                if (code[0] in coordinate_args):
                    command_buffer.append(code)
                else:
                    command_arr.append(command_buffer)
                    command_buffer = []
                    command_buffer.append(code)

        command_arr = command_arr[1:]

        return command_arr