'''
Created on Jan 9, 2016

@author: kenny
'''
import wpilib

class DistanceSpeedController(object):
    '''
    classdocs
    '''


    def __init__(self, controller, encoder):
        '''
        Constructor
        '''
        self.sp = controller
        self.enc = encoder
        self.lastdist = 0
        self.currdist = 0
        self.running = False
         
    def godistance(self, dist):
        self.lastdist = dist
        self.running = True
        if self.currdist <= self.lastdist and self.running:
            self.currdist += self.enc.getDistance()
            self.sp.set(0.75)
        self.sp.set(0)
        
    def gotime(self, speed, time):
        self.sp.set(speed)
        wpilib.Timer.delay(time)
        self.sp.set(0)
    
    def stop(self):
        self.running = False
        self.sp.set(0)
    
    def set(self, speed):
        self.sp.set(speed)