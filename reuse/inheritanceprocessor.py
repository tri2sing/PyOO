'''
Created on Oct 5, 2015

@author: Sameer Adhikari
'''
import abc
import os
import shutil
import zipfile

class InheritanceProcessor(object):
    '''
    This is a class which handles provides the mechanism  
    to apply uniform processing to all files inside a zip.
    What the functionality is will be provided by a sub-class.
    '''
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, zipname):
        self.zipname = zipname
        # Assumption: last 4 letters are '.zip', so we ignore them
        self.tempdir = 'unzipped-{}'.format(zipname[:-4]) 
        
    def _full_filename(self, filename):
        return os.path.join(self.tempdir, filename)
    
    @abc.abstractclassmethod
    def process_files(self):
        '''
        Any sub-class that want to provide processing for
        the contents of zip file must implement this method.
        '''
        
    def process_zip(self):
        self.unzip_files()
        # The process_files method is implemented by a sub-class.
        # The method process each file inside the zip individually.
        self.process_files()
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