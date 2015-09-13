'''
Created on Sep 12, 2015

@author: Sameer Adhikari
'''

from exception.authenticator import authenticator
from exception.authorizer import authorizer
import exception.exceptions as exceptions

#authenticator.add_user("sameer", "sameer")
authenticator.add_user("sameer", "sameerpassword")
authorizer.add_permission_name("test program")
authorizer.add_permission_name("change program")
authorizer.grant_user_permission("test program", "sameer")


class Driver(object):
    '''
    Menu-based editor to test the exception package
    '''
    def __init__(self):
        self.username = None
        self.menu_map = {
                "login": self.login,
                "test": self.test,
                "change": self.change,
                "quit": self.quit
                }
    
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = authenticator.login(username, password)
            except exceptions.InvalidUsername:
                print("The username does not exist")
            except exceptions.InvalidPassword:
                print("The password is not valid")
            else:
                self.username = username
    
    def is_permitted(self, permission_name):
        try:
            authorizer.check_user_permission(permission_name, self.username)
        except exceptions.NotLoggedInError as e:
            print('{} is not logged in'.format(e.username))
            return False
        except PermissionError as e:
            print('User: {} does not have permission: {}'.format(self.username, permission_name))
            return False
        else:
            return True
            
    def test(self):
        if self.is_permitted('test program'):
            print('Testing program')
        else:
            print('Not allowed to test program')
            
    
    def change(self):
        if self.is_permitted('change program'):
            print('Changing program')
        else:
            print('Not allowed to change program')
            
                    
    def quit(self):
        raise SystemExit()
    
    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
                Please enter a command:
                login\tLogin
                test\tTest the program
                change\tChange the program
                quit\tQuit
                """
                )
                answer = input("\t\tenter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(
                        answer))
                else:
                    func()
        finally:
            print("Thank you for testing the exception package")

Driver().menu()
