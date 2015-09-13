'''
Created on Sep 10, 2015

@author: Sameer Adhikari
'''

class AuthException(Exception):
    def __init__(self, username):
        super().__init__(username)
        self.username = username
        
class UserNameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

