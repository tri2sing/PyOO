'''
Created on Nov 29, 2015

@author: Sameer Adhikari
'''
import sys
import time

# Receiver classes that perform the actual work in the command pattern

class Window(object):
    ''' Example of a receiver'''
    def exit(self):
        sys.exit(0)
        
class Document(object):
    ''' Example of a receiver'''
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_content = 'This is the unchanging content added to the file in every save'
        
    def save(self):
        with open(self.file_name, 'a') as file:
            file.write('Saved at ' + time.strftime("%c") + ': ' + self.file_content + '\n')