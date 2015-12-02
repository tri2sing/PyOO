'''
Created on Nov 30, 2015

@author: Sameer Adhikari
'''


import abc
from patterns.abstractfactory.products import \
    USADateFormatter, USACurrencyFormatter, \
    FranceDateFormatter, FranceCurrencyFormatter

class AbstractFormatterFactory(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def date_formatter(self):
        ''' '''
        
    @abc.abstractmethod
    def currency_formatter(self):
        ''' '''
        
        
class USAFormatterFactory(AbstractFormatterFactory):

    def date_formatter(self):
        return USADateFormatter()
    
    def currency_formatter(self):
        return USACurrencyFormatter()
    

class FranceFormatterFactory(AbstractFormatterFactory):

    def date_formatter(self):
        return FranceDateFormatter()
    
    def currency_formatter(self):
        return FranceCurrencyFormatter()
    
        
