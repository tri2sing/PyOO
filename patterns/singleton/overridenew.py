'''
Created on Nov 24, 2015

@author: Sameer Adhikari
'''

class SingletonNew(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SingletonNew, cls).__new__(cls, *args, **kwargs)
        return cls.instance
    
    
if __name__ == '__main__':
    a = SingletonNew()
    b = SingletonNew()
    print(a is b)
    print(hex(id(a)))
    print(hex(id(a)))
    
        
    