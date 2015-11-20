'''
Created on Nov 17, 2015

@author: Sameer Adhikari
'''

class Node(object):
    '''
    Class that represents a tag in the XML document tree.
    '''


    def __init__(self, tag_name, parent=None):
        '''
        Constructor
        '''
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ''
        
    def __str__(self):
        if self.text:
            return self.tag_name + ': ' + self.text
        else:
            return self.tag_name
        