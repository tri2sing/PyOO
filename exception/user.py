'''
Created on Sep 10, 2015

@author: Sameer Adhikari
'''

import hashlib

class User(object):
    '''
    Represents a user of the system.
    '''

    def __init__(self, username, password):
        '''
        Create a new user with the given username.
        Encrypt and store the password.
        '''
        self.username = username
        self.encrypted_password = self._encrypt_password(password)
        self.is_logged_in = False
        
        
    def _encrypt_password(self, password):
        '''
        Encrypt the password with username and return the sha digest.
        '''
        hash_string = (self.username + password)
        hash_string = hash_string.encode('utf8')
        return hashlib.sha256(hash_string).hexdigest()
    
    def check_password(self, password):
        '''
        Checks if the provided password matches the one stored for this user.
        '''
        encrypted_value = self._encrypt_password(password)
        return encrypted_value == self.encrypted_password
        
        
        