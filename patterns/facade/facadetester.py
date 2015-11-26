'''
Created on Nov 25, 2015

@author: Sameer Adhikari
'''

from patterns.facade.car import Car

if __name__ == '__main__':
    elantra = Car()
    elantra.turn_key()
    elantra.jump_battery()
    elantra.turn_key()
