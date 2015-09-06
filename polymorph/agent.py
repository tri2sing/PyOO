'''
Created on Sep 5, 2015

@author: Sameer Adhikari
'''

from polymorph.property import get_valid_input
from polymorph.rentaltypes import HouseRental, ApartmentRental
from polymorph.purchasetypes import HousePurchase, ApartmentPurchase

class Agent(object):
    
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        } 
        
    def __init__(self):
        self.property_list = []
        
    def display_properties(self):
        for item in self.property_list:
            item.display()
            

    def add_property(self):
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ", ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
    
if __name__ == '__main__':
    agent = Agent()
    agent.add_property()
    agent.add_property()
    agent.display_properties()