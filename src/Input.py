'''
Created on Jan 9, 2016

@author: kenny
'''

import wpilib

class Input(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.j = wpilib.Joystick(0)
        
    def teleop(self):
        
_instance = None

def getinstance():
    global _instance
    if _instance is None:
        _instance = Input()
    return _instance