""" Simulates CNC machine control. """

import time

class MachineClient:
    def home(self):
        """ Moves machine to home position. """
        print("Moving to home.")
        
    def move(self, x, y, z):
        """ Uses linear movement to move spindle to given XYZ coordinates.

        Args:
        x (float): X axis absolute value [mm]
        y (float): Y axis absolute value [mm]
        z (float): Z axis absolute value [mm]
        """
        print("Moving to X={:.3f} Y={:.3f} Z={:.3f} [mm].".format(x, y, z))

    def move_relative(self, x, y, z):
        """ Uses linear movement to move spindle relative to current coordinates.

        Args:
        x (float): X axis relative value [mm]
        y (float): Y axis relative value [mm]
        z (float): Z axis relative value [mm]
        """
        print("Moving X={:.3f} Y={:.3f} Z={:.3f} [mm].".format(x, y, z))


    def move_x(self, value):
        """ Move spindle to given X coordinate. Keeps current Y and Z unchanged.

        Args:
        value (float): Axis absolute value [mm]
        """
        print("Moving X to {:.3f} [mm].".format(value))

    def move_y(self, value):
        """ Move spindle to given Y coordinate. Keeps current X and Z unchanged.

        Args:
        value(float): Axis absolute value [mm]
        """
        print("Moving Y to {:.3f} [mm].".format(value))

    def move_z(self, value):
        """ Move spindle to given Z coordinate. Keeps current X and Y unchanged.

        Args:
        value (float): Axis absolute value [mm]
        """
        print("Moving Z to {:.3f} [mm].".format(value))

    def move_x_relative(self, value):
        """ Move spindle to relative X coordinate. Keeps current Y and Z unchanged.

        Args:
        value (float): Axis relative value [mm]
        """
        print("Moving X {:.3f} [mm] relative to current position.".format(value))

    def move_y_relative(self, value):
        """ Move spindle to relative Y coordinate. Keeps current X and Z unchanged.

        Args:
        value(float): Axis relative value [mm]
        """
        print("Moving Y {:.3f} [mm] relative to current position.".format(value))

    def move_z_relative(self, value):
        """ Move spindle to relative Z coordinate. Keeps current X and Y unchanged.

        Args:
        value (float): Axis relative value [mm]
        """
        print("Moving Z {:.3f} [mm] relative to current position.".format(value))

    def set_feed_rate(self, value):
        """ Set spindle feed rate.
        G-code: F.

        Args:
        value (float): Feed rate [mm/s]
        """
        print("Using feed rate {} [mm/s].".format(value))

    def set_spindle_speed(self, value):
        """ Set spindle rotational speed.
        G-code: S.

        Args:
        value (int): Spindle speed [rpm]
        """
        print("Using spindle speed {} [mm/s].".format(value))

    def change_tool(self, tool_name):
        """ Change tool with given name.
        G-code : M06.

        Args:
        tool_name (str): Tool name.
        """
        print("Changing tool '{:s}'.".format(tool_name))

    def coolant_on(self):
        """ Turns spindle coolant on. """
        print("Coolant turned on.")

    def coolant_off(self):
        """ Turns spindle coolant off. G-code: M09."""
        print("Coolant turned off.")

    def set_rapid_positioning(self):
        """ Set rapid positioning. G-code: G00 """
        print("Set rapid positioning.")

    def plane_XY(self):
        """ Set interpolation plane to XY. G-code: G17 """
        print("Set interpolation plane to XY.")

    def set_millimeters(self):
        """ Set programming to use millimeters. G-code: G21 """
        print("Set programming to use millimeters.")

    def turn_off_cutter_radius_c(self):
        """ Turn off cutter radius compensation. G-code: G40 """
        print("Turn off cutter radius compensation.")

    def tool_length_c_cancel(self):
        """ Cancel tool length offset compensation. G-code: G49 """
        print("Cancel tool length offset compensation.")

    def canned_cycle_cancel(self):
        """ Cancel canned cycle. G-code: G80 """
        print("Cancel canned cycle.")

    def set_feed_rate_pm(self):
        """ Set feed rate per minute. G-code: G94 """
        print("Set feed rate per minute.")

    def tool_select(self, tool_name):
        """ Select tool. G-code = T."""
        print("Select tool {}".format(tool_name))

    def set_spindle_on(self):
        """ Set spindle on. G-code: M03. """
        print( "Set spindle on.")

    def set_absolute_programming(self):
        """ Set absolute programming. G-code: G90. """
        print("Set absolute programming.")

    def set_work_coordinate_system(self):
        """ Set work coordinate system. G-code: G54. """
        print("Set work coordinate system.")

    def set_incremental_programming(self):
        """ Set incremental programming. G-code: G91. """
        print("Set incremental programming.")

    def set_linear_interpolation(self):
        """ Set linear interpolation. G-code: G01. """
        print("Set linear interpolation.")

    def stop_spindle(self):
        """ Stop spindle. G-code: M05 """
        print("Stop spindle.")

    def end_program(self):
        """ End program. G-code: M30 """
        print("End program")