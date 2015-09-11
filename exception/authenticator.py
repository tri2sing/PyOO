'''
Created on Sep 10, 2015

@author: Sameer Adhikari
'''

from exception.user import User
from exception.exceptions import UserNameAlreadyExists, PasswordTooShort
from exception.exceptions import InvalidUsername, InvalidPassword

class Authenticator (object):
    '''
    Class the manages log in and out of users.
    '''
    def __init__(self):
        '''
        Construct an authenticator without any users.
        '''
        self.users = {}
        
    def add_user(self, username, password):
        '''
        Add a new user to the authenticator if there are no issues.
        '''
        if username in self.users:
            raise UserNameAlreadyExists(username)
        if len(password) < 8:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)
    
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
        
    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(username, password):
            raise InvalidPassword(username)
        user.is_logged_in = False
        return True


# Default authenticator; exists at the module level
authenticator = Authenticator()
