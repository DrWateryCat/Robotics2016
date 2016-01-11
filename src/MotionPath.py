'''
Created on Jan 10, 2016

@author: kenny
'''
import Drive

class MotionPath(object):
    '''
    classdocs
    '''


    def __init__(self, file):
        '''
        Constructor
        '''
        self.cmdlist = []
        self.index = 0
        
        with open(file) as f:
            self.cmdlist = f.readlines()
        print(len(self.cmdlist))
        
        self.running = True
    
    def run(self):
        try:
            nextcommand = self.cmdlist[self.index]
            self.index += 1
            if nextcommand and self.running:
                if nextcommand[0] is "f":
                    if len(nextcommand) is 3:
                        dist = float(nextcommand[2])
                        Drive.getinstance().forwardtime(dist)
                    else:
                        dist = float(nextcommand[2] + nextcommand[3])  
                        Drive.getinstance().forwardtime(dist)
                        
                elif nextcommand[0] is "b":
                    if len(nextcommand) is 3:
                        dist = float(nextcommand[2])
                        Drive.getinstance().reverse(dist)
                    else:
                        dist = float(nextcommand[2] + nextcommand[3])
                        Drive.getinstance().reverse(dist)      
                
                elif nextcommand[0] is "l":
                    if len(nextcommand) is 3:
                        deg = int(nextcommand[2])
                        Drive.getinstance().left(deg)
                    else:
                        deg = int(nextcommand[2] + nextcommand[3])
                        Drive.getinstance().left(deg)
                        
                elif nextcommand[0] is "r":
                    if len(nextcommand) is 3:
                        deg = int(nextcommand[2])
                        Drive.getinstance().right(deg)
                    else:
                        deg = int(nextcommand[2] + nextcommand[3])
                        Drive.getinstance().right(deg)
                        
                elif nextcommand[0] is "s":
                    Drive.getinstance().stop()
                
                elif nextcommand is None:
                    Drive.getinstance().stop()
                
                else:
                    raise SyntaxError("Invalid syntax: " + nextcommand)
        except:
            if self.running:
                print("Stopped")
            self.running = False