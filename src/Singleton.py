'''
Created on Jan 10, 2016

@author: kenny
'''

class Singleton(type):
    _instances = {}
    
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]