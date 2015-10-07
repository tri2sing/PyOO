'''
Created on Oct 7, 2015

@author: Sameer Adhikari
'''

import sys
import os

from reuse.compositionporcessor import CompositionProcessor

class CompositionReplacer(object):
    '''
    Provides the function to search and replace text in files.
    '''

    def __init__(self, searchpattern, replacepattern):
        self.searchpattern = searchpattern
        self.replacepattern = replacepattern

    def process_files(self, zipprocessor):
        '''
        Does a search and replace on all the files in the temporary directory.
        '''
        for filename in os.listdir(path=zipprocessor.tempdir):
            print('Reading file: {}'.format(zipprocessor._full_filename(filename)))
            with open(zipprocessor._full_filename(filename)) as file:
                contents = file.read()
                contents = contents.replace(self.searchpattern, self.replacepattern)
            print('Writing file: {}'.format(zipprocessor._full_filename(filename)))
            with open(zipprocessor._full_filename(filename), 'w') as file:
                file.write(contents)
                
if __name__ == '__main__':
    print('Command line arguments are: {}'.format(sys.argv))
    compreplace = CompositionReplacer(*sys.argv[2:4])
    CompositionProcessor(sys.argv[1], compreplace).process_zip()
