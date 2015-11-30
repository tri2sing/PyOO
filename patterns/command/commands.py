'''
Created on Nov 29, 2015

@author: Sameer Adhikari
'''

import abc

class AbstractCommand():
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def execute(self):
        ''' Method presented to the invokers'''
        
        
class SaveCommand(AbstractCommand):
    def __init__(self, document):
        self.document = document
        
    def execute(self):
        self.document.save()
        
class ExitCommand(AbstractCommand):
    def __init__(self, window):
        self.window = window
        
    def execute(self):
        self.window.exit()