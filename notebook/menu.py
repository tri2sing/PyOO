'''
Created on Sep 2, 2015

@author: Sameer Adhikari
'''
import abc, sys
from notebook.book import Notebook
from notebook.note import Note

class Menu(object):
    '''Abstract class for the interface that the  
    user has to work with notebooks and notes.
    The interface will vary between a CLI and GUI.
    This class enforces the methods to implement.
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        '''
        '''
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.find_notes,
            '3': self.add_new_note,
            '4': self.modify_note,
            '5': self.quit
        }
        
    @abc.abstractmethod
    def display_menu(self):
        '''Displays the menu to the user.
        Returns the choice as string.
        '''
        
    @abc.abstractmethod
    def display_notes(self, notes=None):
        '''Displays the notes to the user. 
        '''
        
    @abc.abstractmethod
    def find_notes(self):
        '''Asks the user for a search pattern.
        Displays any matching note found.
        '''
        
    @abc.abstractmethod
    def add_new_note(self):
        '''Modifies the text and tags for a note.
        '''
    @abc.abstractmethod
    def modify_note(self):
        '''Modifies the text and tags for a note.
        '''
        
    def quit(self):
        '''Exit from the notebook.
        '''
        sys.exit(0)