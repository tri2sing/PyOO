'''
Created on Nov 20, 2015

@author: Sameer Adhikari
'''
from patterns.strategy.genericseriesgenerator import GenericSeriesGenerator
from patterns.strategy.specificseriesgenerators import *

if __name__ == '__main__':
    
    limit = 15
    print('The limit is {}'.format(limit))
    print('')
    
    odd_gen = GenericSeriesGenerator(odd_series_generator)
    odd_gen.calculate(limit)
    odd_gen.output()
    
    even_gen = GenericSeriesGenerator(even_series_generator)
    even_gen.calculate(limit)
    even_gen.output()
    
    fib_gen = GenericSeriesGenerator(fibonacci_series_generator)
    fib_gen.calculate(limit)
    fib_gen.output()
    