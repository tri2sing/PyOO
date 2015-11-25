'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

from patterns.adapter.dog import Dog

class DogAdapter(object):
    '''Adapts the dog class through encapsulation.'''

    def __init__(self, canine):
        self.canine = canine
        
    def make_noise(self):
        '''Only adapted method'''
        return self.canine.bark()
    
    def __getattr__(self, attr):
        '''Delegate everything other than adapted method to the object'''
        return getattr(self.canine, attr)
    
