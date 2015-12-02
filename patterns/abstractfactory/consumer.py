'''
Created on Dec 1, 2015

@author: Sameer Adhikari
'''
from patterns.abstractfactory.configurer import factory

if __name__ == '__main__':
    print('Hello')
    print('The consumer does not control the factory it gets')
    print(type(factory).__name__)
    print('But, it can use the products as they adhere to the interface')
    date_formatter = factory.date_formatter()
    currency_formatter = factory.currency_formatter()
    print(date_formatter.format_date(13, 9, 5))
    print(currency_formatter.format_currency(1579, 3))
    print('Done')