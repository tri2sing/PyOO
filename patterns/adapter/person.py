'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

class Person(object):
    '''
    One type of creature that makes some noise.
    '''

    def __init__(self, name):
        self.name = name
        
    def make_noise(self):
        return 'hello'