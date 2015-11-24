'''
Created on Nov 24, 2015

@author: Sameer Adhikari
'''

class SingletonMeta(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        '''
        Method that gets invoked when class is called (instantiated)
        Using cls instead of self as the name of the first parameter may 
        appear as an error in Eclipse PyDev, but the program runs fine.
        '''
        if not cls.instance:
            cls.instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.instance

if __name__ == '__main__':
    class ASingleton(metaclass=SingletonMeta):
        pass
    
    a = ASingleton()
    b = ASingleton()
    print(a is b)
    print(hex(id(a)))
    print(hex(id(a)))
        