'''
Created on Nov 29, 2015

@author: Sameer Adhikari
'''

# Classes the initiate the chain that leads to the receivers doing their work.
# These classes are only aware that they have to invoke the abstract command.
# These classes have no visibility into how the commands connects to receivers.

class ToolbarButton(object):
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        
    def click(self):
        # invoke the abstract command without knowing how the command will be set
        print('Simulating the click of a toolbar button')
        self.command.execute()
        
class MenuItem(object):
    def __init__(self, menu_name, menu_item_name):
        self.menu = menu_name
        self.item = menu_item_name

    def choose(self):
        # invoke the abstract command without knowing how the command will be set
        print('Simulating the selction of a menu item')
        self.command.execute()
        
class KeyboardCombination(object):
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier
        
    def keypress(self):
        # invoke the abstract command without knowing how the command will be set
        print('Simulating the press of a keyboard combination')
        self.command.execute()
        
