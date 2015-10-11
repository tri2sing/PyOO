'''
Created on Oct 10, 2015

@author: Sameer Adhikari
'''
from pprint import PrettyPrinter

# Example illustrating mixing keys in a dictionary
# The keys can be any hashable type

randkeys = {}
randkeys['astring'] = 'a string'
randkeys[7] = 'an integer'
randkeys[5.7] = 'a float'
randkeys[('astring', 7)] = 'a tuple'

class AnObject(object):
    def __init__(self, avalue):
        self.avalue = avalue

anobject = AnObject(13)        
randkeys[anobject] = 'an object'
anobject.avalue = 11

alist = [1, 2, 3]
adict = {'a': 1}

try:
    randkeys[alist] = 'a list'
except: 
    print('Unable to use a list as a key')

try:
    randkeys[adict] = 'a dict'
except: 
    print('Unable to use a dict as a key')

pp = PrettyPrinter(indent=4)
pp.pprint(randkeys)