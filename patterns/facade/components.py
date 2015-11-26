'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

class Engine(object):
    
    def __init__(self):
        self.engine_spin = 0 #RPM for the engine
        
    def start(self, starter_spin):
        if starter_spin > 2000:
            self.engine_spin = starter_spin // 15
        

class Starter(object):
    
    def __init__(self):
        self.starter_spin = 0 # RPM for the Starter
    
    def start(self, charge_supplied):
        if charge_supplied > 50: # The charge supplied by the battery
            self.starter_spin = 2500 # spin fast
            

class Battery(object):
    def __init__(self):
        self.charge_level = 0 # Level of batter charge in percentage