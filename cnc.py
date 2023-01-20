import sys

import MachineClient as MC
import Parser

COMMAND_TO_MC_STUB = {'G00' : move_logic,
                      'G17' : MC.plane_XY,
                      'G21' : MC.set_millimeters,
                      'G40' : MC.turn_off_cutter_radius_c,
                      'G49' : MC.tool_length_c_cancel,
                      'G80' : MC.canned_cycle_cancel,
                      'G94' : MC.set_feed_rate_pm,
                      'T'   : MC.tool_select,
                      'M06' : MC.change_tool,
                      'S'   : MC.set_spindle_speed,
                      'M03' : MC.set_spindle_on,
                      'G90' : MC.set_absolute_programming,
                      'G54' : MC.set_work_coordinate_system,
                      'G01' : move_logic,
                      'F'   : MC.set_feed_rate,
                      'G91' : MC.set_incremental_programming,
                      'G28' : MC.home
                      }

def main(args):
    parser = Parser.Parser()
    commands = parser.parse_file(args[1])


    print(commands)

def move_logic():
    return


if __name__ == "__main__":
    main(sys.argv)