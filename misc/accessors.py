'''
Created on Sep 12, 2015

@author: Sameer Adhikari
'''

# Technically this example illustrates how to change a class from 
# one form to another without having to change the client.
# But, as it is not possible to two definition of class Color in 
# the same module, we use two classes to show the concept.

# The original class Color allows a user to set an empty string to 
# the name attribute. The goal is to transform it to a form which 
# prevents a user from doing so without having to change their code.

# The magic is in the "property" keyword that presents the new 
# accessor methods as the attribute "name" in the morphed class.

# Even with the "name" property the new form is not bullet-proof.
# A client can access the _name attribute which we cannot prevent.

class ColorNoCheck:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name

class ColorCheck:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise ValueError("Empty color not allowed")
        self._name = name
        
    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)
    
if __name__ == '__main__':
    c1 = ColorNoCheck('ff0000', 'bright red')
    print('1. The name = {}'.format(c1.name))
    c1.name = ''
    print('Execution proceeds without error')
    
    c2 = ColorCheck('ff0000', 'bright red')
    print('2. The name = {}'.format(c2.name))
    c2.name = ''