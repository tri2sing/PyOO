'''
Created on Oct 5, 2015

@author: Sameer Adhikari
'''

import os
import shutil
import zipfile

class InheritanceProcessor(object):
    def __init__(self, zipname):
        self.zipname = zipname
        self.tempdir = 'unzipped-{}'.format(zipname[:-4]) # assumes last 4 letters are '.zip'
        
    def _full_filename(self, filename):
        return os.path.join(self.tempdir, filename)
    
    def process_zip(self):
        self.unzip_files()
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
        for filename in os.listdir(path=self.tempdir):
            file.write(self._full_filename(filename, filename))
        shutil.rmtree(self.tempdir)