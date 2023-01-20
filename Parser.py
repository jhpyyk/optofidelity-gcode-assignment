class Parser:
    def parse_file(self, file_path):
        """
        Parses a G-Code file into arrays of command and its arguments.
        (e.g. [G01, {argument1: value, argument2: value}).

        Args:
        file_path (string): Path to file.

        Returns:
        parsed_commands (array): Arrays of command and its arguments.
        """
        if (file_path[-6:] != '.gcode'):
            print("Invalid argument: not a G-Code (.gcode) file")
            return

        lines = self.parse_file_to_lines(file_path)
        commands = self.parse_lines_to_commands(lines)
        parsed_commands = self.parse_commands(commands)
        merged = self.merge_commands(parsed_commands)
        
        return merged
    
    

    def parse_file_to_lines(self, file_path):
        """ 
        Parses lines from a G-Code file.

        Args:
        file_path (string): Relative path to the G-code file.

        Returns:
        lines (array): Array of all the lines.Each line is split into strings
                       with space being the separator.
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
        coordinate_args = {'X', 'Y', 'Z'}

        for line in lines:
            if (line[0][0] == 'N'):
                line_number = line[0]
                line = line[1:]
            
            arranged = self.arrange_commands(line)
            arranged.append('$newline')
            command_arr.extend(arranged)

        return command_arr

    def arrange_commands(self, commands):
        arranged = []
        for command in commands:
            if (command[0][0] == 'F'):
                arranged.append(command)

        for command in commands:
            if (command[0][0] == 'S'):
                arranged.append(command)
        
        for command in commands:
            if (command[0][0] == 'T'):
                arranged.append(command)
        
        for command in commands:
            if (command[0][0] == 'M'):
                arranged.append(command)

        for command in commands:
            if (command[0][0] == 'G'):
                arranged.append(command)
        
        for command in commands:
            if (command[0][0] == 'X'):
                arranged.append(command)
        
        for command in commands:
            if (command[0][0] == 'Y'):
                arranged.append(command)

        for command in commands:
            if (command[0][0] == 'Z'):
                arranged.append(command)

        return arranged

    def parse_commands(self, commands):
        """
        Parses commands into form ['G-Code', {'argument': value}].

        Args:
        commands (array): Array of commands in form ['G-code', argument1, ...].

        Returns:
        parsed_commands (array):
        Array of commands in form ['G-Code', {argument (string): value (float)}].
        """
        
        parsed_commands = []
        for command in commands:

            match command[0]:
                case 'G':
                    parsed_commands.append([command])
                case 'T':
                    parsed_commands.append(self.parse_T(command))
                case 'M':
                    parsed_commands.append([command])
                case 'S':
                    parsed_commands.append(self.parse_S_F(command))
                case 'F':
                    parsed_commands.append(self.parse_S_F(command))
                case 'X':
                    parsed_commands.append(self.parse_coordinate(command))
                case 'Y':
                    parsed_commands.append(self.parse_coordinate(command))
                case 'Z':
                    parsed_commands.append(self.parse_coordinate(command))
                case '$':
                    parsed_commands.append([command])
                case _:
                    print("Command {} not implemented".format(command))

        return parsed_commands

    def parse_T(self, command):
        """
        Parses commands starting with a 'T'. T = Tool selection.

        Args:
        command (array): First element is command starting with a 'T'.

        Returns:
        parsed (array): Command in form ['G-Code', {argument (string): value (string)}].
        """

        parsed = [command[0], {'tool_name': command[1:]}]
        return parsed

    def parse_S_F(self, command):
        """
        Parses commands starting with an 'S' or 'F'. S = Speed, F = Feed rate.

        Args:
        command (array): First element is command starting with an 'S' or 'F'.

        Returns:
        parsed (array): Command in form ['G-Code', {argument (string): value (float)}].
        """
        parsed = [command[0], {'value': float(command[1:])}]
        return parsed

    def parse_coordinate(self, command):
        """
        Parses commands starting with an 'X', 'Y' or 'Z'.

        Args:
        command (string): First letter is 'X', 'Y' or 'Z'.

        Returns:
        parsed (array): Command in form ['G-Code', {argument (string): value (float)}].
        """
        parsed = [command[0], {command[0].lower(): float(command[1:])}]
        return parsed

    def merge_commands(self, commands):
        """
        Merges move commands.

        Args:
        commands (array): Array of commands.

        Returns:
        merged_commands (array): Merged commands.
        """
        merged_commands = []
        buffer = ['move', {}]
        for command in commands:
            if (command[0] == '$newline'):
                if (len(buffer[1]) > 0):
                    merged_commands.append(buffer)
                    buffer = ['move', {}]
            elif (command[0][0] in {'X', 'Y', 'Z'}):
                buffer[1].update(command[1])
            else:
                merged_commands.append(command)
        
        return merged_commands


