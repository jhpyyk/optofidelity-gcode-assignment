import MachineClient
import Parser
    
class Runner():
    def __init__(self, file_path):
        self.tool = ""
        self.last_x = 0.0
        self.last_y = 0.0
        self.last_z = 0.0
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
                              'G90' : self.machine_client.set_absolute_programming,
                              'G54' : self.machine_client.set_work_coordinate_system,
                              'G01' : self.machine_client.set_linear_interpolation,
                              'F'   : self.machine_client.set_feed_rate,
                              'G91' : self.machine_client.set_incremental_programming,
                              'G28' : self.machine_client.home,
                              'move': self.move_logic,
                              'M09' : self.machine_client.coolant_off,
                              'M05' : self.machine_client.stop_spindle,
                              'M30' : self.machine_client.end_program}


        self.parser = Parser.Parser()
        self.commands = self.parser.parse_file(file_path)

    def run_simulation(self):
        for command in self.commands:
            if (len(command) > 1):
                self.command_to_mc[command[0]](**command[1])
            else:
                self.command_to_mc[command[0]]()

    def move_logic(self, **kwargs):

        return

    def tool_select(self, tool_name):
        self.tool = tool_name

    def tool_change(self):
        self.machine_client.change_tool(self.tool)     