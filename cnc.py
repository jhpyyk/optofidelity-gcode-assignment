import sys

import MachineClient as MC
import Parser


def main(args):
    command_to_mc = {'G00' : MC.MachineClient.set_rapid_positioning,
                     'G17' : MC.MachineClient.plane_XY,
                     'G21' : MC.MachineClient.set_millimeters,
                     'G40' : MC.MachineClient.turn_off_cutter_radius_c,
                     'G49' : MC.MachineClient.tool_length_c_cancel,
                     'G80' : MC.MachineClient.canned_cycle_cancel,
                     'G94' : MC.MachineClient.set_feed_rate_pm,
                     'T'   : MC.MachineClient.tool_select,
                     'M06' : MC.MachineClient.change_tool,
                     'S'   : MC.MachineClient.set_spindle_speed,
                     'M03' : MC.MachineClient.set_spindle_on,
                     'G90' : MC.MachineClient.set_absolute_programming,
                     'G54' : MC.MachineClient.set_work_coordinate_system,
                     'G01' : MC.MachineClient.set_linear_interpolation,
                     'F'   : MC.MachineClient.set_feed_rate,
                     'G91' : MC.MachineClient.set_incremental_programming,
                     'G28' : MC.MachineClient.home,
                     'X'   : move_logic,
                     'Y'   : move_logic,
                     'Z'   : move_logic}


    parser = Parser.Parser()
    commands = parser.parse_file(args[1])


    print(commands)

def move_logic():
    return


if __name__ == "__main__":
    main(sys.argv)