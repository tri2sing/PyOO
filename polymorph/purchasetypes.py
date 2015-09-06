'''
Created on Sep 5, 2015

@author: Sameer Adhikari
'''

from polymorph.purchase import Purchase
from polymorph.house import House
from polymorph.apartment import Apartment

class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    
    