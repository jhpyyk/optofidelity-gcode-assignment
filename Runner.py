import time

import MachineClient
import Parser
    
class Runner():
    def __init__(self, file_path):
        self.tool = ""
        self.last_x = 0.0
        self.last_y = 0.0
        self.last_z = 0.0
        self.absolute = None
        self.machine_client = MachineClient.MachineClient()
        self.command_to_mc = {'G00' : self.machine_client.set_rapid_positioning,
                              'G17' : self.machine_client.plane_XY,
                              'G21' : self.machine_client.set_millimeters,
                              'G40' : self.machine_client.turn_off_cutter_radius_c,
                              'G49' : self.machine_client.tool_length_c_cancel,
                              'G80' : self.machine_client.canned_cycle_cancel,
                              'G94' : self.machine_client.set_feed_rate_pm,
                              'T'   : self.tool_select,
                              'M06' : self.tool_change,
                              'S'   : self.machine_client.set_spindle_speed,
                              'M03' : self.machine_client.set_spindle_on,
                              'G90' : self.set_absolute,
                              'G54' : self.machine_client.set_work_coordinate_system,
                              'G01' : self.machine_client.set_linear_interpolation,
                              'F'   : self.machine_client.set_feed_rate,
                              'G91' : self.set_incremental,
                              'G28' : self.machine_client.home,
                              'move': self.move_logic,
                              'M09' : self.machine_client.coolant_off,
                              'M05' : self.machine_client.stop_spindle,
                              'M30' : self.machine_client.end_program}


        self.parser = Parser.Parser()
        self.commands = self.parser.parse_file(file_path)

    def run_simulation(self):
        """ Run all commands with 1 second delay in between. """
        for command in self.commands:
            if (len(command) > 1):
                self.command_to_mc[command[0]](**command[1])
            else:
                self.command_to_mc[command[0]]()

            time.sleep(1)

    def move_logic(self, **kwargs):
        """ Choose move function. """
        if (len(kwargs) > 1):
            self.move_triple(**kwargs)

        if (len(kwargs) == 1):
            self.move_single(**kwargs)


    def tool_select(self, tool_name):
        self.tool = tool_name

    def tool_change(self):
        self.machine_client.change_tool(self.tool)

    def set_absolute(self):
        self.absolute = True
        self.machine_client.set_absolute_programming()

    def set_incremental(self):
        self.absolute = False
        self.machine_client.set_incremental_programming()

    def move_triple(self, **kwargs):
        """ Choose move function in MachineClient. Set last coordinates. """
        if ('x' not in kwargs):
            kwargs.update({'x': self.last_x})
        if ('y' not in kwargs):
            kwargs.update({'y': self.last_y})
        if ('z' not in kwargs):
            kwargs.update({'z': self.last_z})
        if (self.absolute):
            self.machine_client.move(**kwargs)
        else:
            self.machine_client.move_relative(**kwargs)
        self.last_x = kwargs['x']
        self.last_y = kwargs['y']
        self.last_z = kwargs['z']

    def move_single(self, **kwargs):
        """ Choose move function in MachineClient. Set last coordinates. """
        if ('x' in kwargs):
            if (self.absolute):
                self.machine_client.move_x(kwargs['x'])
            else:
                self.machine_client.move_x_relative(kwargs['x'])
            self.last_x = kwargs['x']
        if ('y' in kwargs):
            if (self.absolute):
                self.machine_client.move_y(kwargs['y'])
            else:
                self.machine_client.move_y_relative(kwargs['y'])
            self.last_x = kwargs['y']
        if ('z' in kwargs):
            if (self.absolute):
                self.machine_client.move_z(kwargs['z'])
            else:
                self.machine_client.move_z_relative(kwargs['z'])
            self.last_x = kwargs['z']
