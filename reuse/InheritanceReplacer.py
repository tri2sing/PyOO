'''
Created on Oct 7, 2015

@author: Sameer Adhikari
'''

import sys
import os

from reuse.inheritanceprocessor import InheritanceProcessor

class InheritanceReplacer(InheritanceProcessor):
    '''
    Provides the function to search and replace text in files.
    '''

    def __init__(self, zipname, searchpattern, replacepattern):
        super().__init__(zipname)
        self.searchpattern = searchpattern
        self.replacepattern = replacepattern

    def process_files(self):
        '''
        Does a search and replace on all the files in the temporary directory.
        '''
        for filename in os.listdir(path=self.tempdir):
            print('Reading file: {}'.format(self._full_filename(filename)))
            with open(self._full_filename(filename)) as file:
                contents = file.read()
                contents = contents.replace(self.searchpattern, self.replacepattern)
            print('Writing file: {}'.format(self._full_filename(filename)))
            with open(self._full_filename(filename), 'w') as file:
                file.write(contents)
                
if __name__ == '__main__':
    print('Command line arguments are: {}'.format(sys.argv))
    InheritanceReplacer(*sys.argv[1:4]).process_zip()   