#!/usr/bin/env python3

import wpilib
from MotionPath import MotionPath

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.autopath = MotionPath("motion.txt")

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.autopath.run()
        #Allow time to update
        wpilib.Timer.delay(0.2)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        pass

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass
    
    def disabledInit(self):
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)
