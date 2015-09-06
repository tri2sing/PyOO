'''
Created on Sep 5, 2015

@author: Sameer Adhikari
'''
from polymorph.rental import Rental
from polymorph.house import House
from polymorph.apartment import Apartment

# The order of inherited classes is important for the
# call sequence of the display method.  If House is
# put before Rental the Rental.display() would not
# get called, as the route would be House -> Property, 
# and then the sequence would terminate.

class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

        
if __name__ == '__main__':
#     init = HouseRental.prompt_init()
#     house = HouseRental(**init)
#     house.display()
    
    init2 = ApartmentRental.prompt_init()
    apt = ApartmentRental(**init2)
    apt.display()