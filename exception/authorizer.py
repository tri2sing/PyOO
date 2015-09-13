'''
Created on Sep 11, 2015

@author: Sameer Adhikari
'''
from exception.exceptions import InvalidUsername, NotLoggedInError
from exception.authenticator import authenticator

class Authorizer(object):
    '''
    Represents map of permissions to users.
    '''
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}
        
    def add_permission_name(self, permission_name):
        '''
        Create a permission that a set of users can have.
        '''
        try:
            permission_set = self.permissions[permission_name]
        except:
            # Permission does not exist, so add it
            self.permissions[permission_name] = set()
        else:
            raise PermissionError("Permission {} already exists".format(permission_name))
        
    def grant_user_permission(self, permission_name, username): 
        '''
        Grant the permission given by the name to the user.
        '''  
        try:
            permission_set = self.permissions[permission_name]
        except KeyError:
            raise PermissionError("Permission {} does not exist".format(permission_name))
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            permission_set.add(username)
    
    def check_user_permission(self, permission_name, username):
        '''
        Check whether a user has the specified permission.
        '''
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError("User {} is not logged in".format(username))
        try:
            permission_set = self.permissions[permission_name]
        except KeyError:
            raise PermissionError("Permission {} does not exist".format(permission_name))
        else:
            if username not in permission_set:
                raise PermissionError("User {} does not have permission".format(username))
            else:
                return True 
            
# Default authorizer defined at the module level
# It used the default authenticator 
authorizer = Authorizer(authenticator)