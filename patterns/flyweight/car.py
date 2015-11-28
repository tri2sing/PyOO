'''
Created on Nov 28, 2015

@author: Sameer Adhikari
'''

class Car(object):
    '''Class the uses the model flyweight '''
    
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial
    
    
    
