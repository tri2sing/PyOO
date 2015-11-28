'''
Created on Nov 28, 2015

@author: Sameer Adhikari
'''
from patterns.flyweight.carmodel import CarModel
from patterns.flyweight.car import Car

import gc

if __name__ == '__main__':
    # create flyweights
    dx = CarModel("FIT DX")
    lx1 = CarModel("FIT LX", air=True, tilt=True, cruise_control=True, power_locks=True)
    
    # use flyweights
    car1 = Car(dx, 'blue', '12345')
    car2 = Car(dx, 'black', '12346')
    car3 = Car(lx1, 'brown', '12347')
    
    # demonstrate use of weak reference
    del(lx1)
    del(car3)
    gc.collect()
    try:
        print('Id of lx1 = {}'.format(id(lx1)))
    except:
        print('lx1 has been garbage collected')
        
    # demonstrate use of flyweight
    lx1 = CarModel("FIT LX", air=True, tilt=True, cruise_control=True, power_locks=True)
    print('Id of lx1 = {}'.format(id(lx1)))
    lx2 = CarModel("FIT LX")
    print('Id of lx1 = {}'.format(id(lx1)))
    print('Id of lx2 = {}'.format(id(lx2)))
    print('lx2.air value (even though we did not initialize it) = {}'.format(lx2.air))
    
    
    
    
