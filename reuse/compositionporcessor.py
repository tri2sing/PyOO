'''
Created on Oct 7, 2015

@author: Sameer Adhikari
'''

import os
import shutil
import zipfile

class CompositionProcessor(object):
    '''
    This is a class which handles provides the mechanism  
    to apply uniform processing to all files inside a zip.
    What the functionality is will be provided by a sub-class.
    '''
    
    def __init__(self, zipname, processor):
        self.zipname = zipname
        # Assumption: last 4 letters are '.zip', so we ignore them
        self.tempdir = 'unzipped-again-{}'.format(zipname[:-4]) 
        self.processor = processor
        
    def _full_filename(self, filename):
        return os.path.join(self.tempdir, filename)
    
    def process_zip(self):
        self.unzip_files()
        # The process_files method is implemented by a sub-class.
        # The method process each file inside the zip individually.
        self.processor.process_files(self)
        self.zip_files()
        
    def unzip_files(self):
        os.mkdir(self.tempdir)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.tempdir)
        finally:
            zip.close()
            
    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        # Assumption: all files are in this folder and there are no sub-folders
        for filename in os.listdir(path=self.tempdir):
            file.write(self._full_filename(filename))
        shutil.rmtree(self.tempdir)