'''
Created on Nov 17, 2015

@author: Sameer Adhikari
'''

import patterns.state.states as sts

class Parser(object):
    '''
    Class that represents the XML parser.
    '''


    def __init__(self, input_string):
        '''
        Constructor
        '''
        self.input_string = input_string
        self.root_node = None # The root of the tree of tags, which is set once
        self.current_node = None # The node to which to the next discovered children are added
        self.state = sts.StartState()
        
    def process(self, input_string):
        remaining_string = self.state.process(input_string, self)
        if remaining_string:
            self.process(remaining_string)
            
    def start(self):
        self.process(self.input_string)
        