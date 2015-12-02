'''
Created on Dec 2, 2015

@author: Sameer Adhikari
'''

# Class that represents the common operations between 
# composite and leaf/primitive nodes in the hierarchy
# This is  a simulation which lacks a lot of operations
class Component(object):
    def __init__(self, name):
        self.name = name
        
    def move(self, destination_path):
        destination_folder = get_folder(destination_path)
        del self.parent.children[self.name] # Remove folder from current location
        destination_folder.children[self.name] = self # Move to new folder location
        self.parent = destination_folder # Set up traversal path to root
        
    def delete(self):
        del self.parent.children[self.name] # Remove folder from current location
        
    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child


# Class that represent the composite node in the hierarchy
class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {} # A folder can have folders or files


# Class the represents the leaf/primitve node, which does not have children
class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

# Module level variable to represent the root of a filesystem
root = Folder('')     

# This function causes a cyclic dependency.
# It operates on component but requires a root folder.
# But, folder is a subclass of component.
# Python's dynamic typing and handling of module variables helps out.

def get_folder(path):
    ''' Returns the folder node to which the string path refers '''
    folders_along_path = path.split('/')[1:] # Ignore the initial empty string from split
    node = root # Start at the top
    for folder_name in folders_along_path: # Traverse down the tree
        node = node.children[folder_name] # Get pointer to the node at the current tree level
    return node    
    

