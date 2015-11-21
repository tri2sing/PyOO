'''
Created on Nov 20, 2015

@author: Sameer Adhikari
'''

class GenericSeriesGenerator(object):
    '''
    '''
    def __init__(self, generator):
        '''
        The generator parameter is a callable that does the actual work.
        '''
        self.generator = generator
        self.series = []
        
    def calculate(self, limit):
        '''
        Calculate all the numbers in the series below the limit.
        '''
        self.series = self.generator(limit)
        
    def output(self):
        '''
        Print the series that was generated with the name of the generator
        '''
        print(self.generator.__name__)
        print(self.series)
        print('')