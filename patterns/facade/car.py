'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''
from patterns.facade.components import *

class Car(object):
    '''
    Facade that the user sees to all the other components: battery, starter, and engine.
    '''

    def __init__(self):
        self.battery = Battery()
        self.starter = Starter()
        self.engine = Engine()
        
    def turn_key(self):
        self.starter.start(self.battery.charge_level) # use the batter to turn starter
        self.engine.start(self.starter.starter_spin) # use starter to spin the engine
        if self.engine.engine_spin > 0:
            print('Engine start succeeded')
        else:
            print('Engine start failed')
            
    def jump_battery(self):
        self.battery.charge_level = 75
        print('Jumped the battery')
        
        
        