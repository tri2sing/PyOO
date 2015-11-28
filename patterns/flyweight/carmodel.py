'''
Created on Nov 28, 2015

@author: Sameer Adhikari
'''

from weakref import WeakValueDictionary

class CarModel(object):
    '''A factory class to create flyweights and keep track of those created'''
    _models = WeakValueDictionary()
    
    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            print('__new__ being done first time for model = {}'.format(model_name))
            model = super().__new__(cls)
            cls._models[model_name] = model
        else:
            print('__new__ already done earlier for model = {}'.format(model_name))
        return model
        
        
    def __init__(self, model_name, air=False, tilt=False, 
                 cruise_control=False, power_locks=False):
        ''' '''
        if not hasattr(self, 'init_done'): # Prevent running when an instance already exists
            print('__init__ being done first time for model = {}'.format(model_name))
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise = cruise_control
            self.power_locks = power_locks
            self.init_done = True
        else:
            print('__init__ already done earlier for model = {}'.format(model_name))
            
            
            
            
    