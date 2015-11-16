'''
Created on Nov 13, 2015

@author: Sameer Adhikari
'''


class Subject:
    '''
    The observed class.
    '''
    def __init__(self):
        self._data = 0
        self.observers = []
        
    def attach(self, observer):
        '''
        Add an observer for this subject.
        The observer should be a callable.
        '''
        self.observers.append(observer)
    
    def _update_observers(self):
        for observer in self.observers:
            observer()
            
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self._update_observers()
        
    