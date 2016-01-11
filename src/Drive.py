'''
Created on Jan 9, 2016

@author: kenny
'''
import Singleton
from DistanceSpeedController import DistanceSpeedController
import wpilib
class Drive(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.sp = DistanceSpeedController(wpilib.VictorSP(0), wpilib.Encoder(0, 1))
        
    def forward(self, dist=None):
        print("Going forward for " + str(dist) + "feet")
        
    def forwardtime(self, time):
        print("Going forward for " + str(time) + " seconds")
        self.sp.gotime(0.75, time)
        
_instance = None

def getinstance():
    global _instance
    if _instance is None:
        _instance = Drive()
    return _instance