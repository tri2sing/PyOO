'''
Created on Sep 3, 2015

@author: Sameer Adhikari
'''

from notebook.menu import Menu
from notebook.book import Notebook

class MenuCLI(Menu):
    '''A class that provides a command line interface for the menu.
    '''


    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.display_notes,
            '2': self.find_notes,
            '3': self.add_new_note,
            '4': self.modify_note,
            '5': self.quit
        }
        Menu.__init__(self, self.notebook, self.choices)

    def display_menu(self):
        '''Displays the menu to the user.
        Returns the choice as string.
        '''
        print('''
        Notebook Menu
        
        1. Show Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        ''')
        return input('\tEnter a choice: ')
        
    def display_notes(self, notes=None):
        '''Displays the notes to the user. 
        '''
        
    def find_notes(self):
        '''Asks the user for a search pattern.
        Displays any matching note found.
        '''
        
    def add_new_note(self):
        '''Modifies the text and tags for a note.
        '''
    def modify_note(self):
        '''Modifies the text and tags for a note.
        '''

if __name__ == '__main__':
    menu_cli = MenuCLI()   
    print(menu_cli.notebook)
    print(menu_cli.choices)
    menu_cli.run()
