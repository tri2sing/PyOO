'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

class Dog(object):
    '''
    Another creature that makes some noise
    '''

    def __init__(self, name):
        self.name = name
        
    def bark(self):
        return 'woof'