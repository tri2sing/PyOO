'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

class CreaturAdapter(object):
    '''Generic adapter for any creature that makes a sound'''

    def __init__(self, creature, make_noise):
        '''
        creature: object that makes the sound
        make_noise: the object's function that emits noise
        '''
        self.creature = creature
        self.make_noise = make_noise
    
    def __getattr__(self, attr):
        '''Delegate everything other than adapted method to the object'''
        return getattr(self.creature, attr)
    
    