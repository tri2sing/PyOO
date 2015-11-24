'''
Created on Nov 24, 2015

@author: Sameer Adhikari
'''

class SingletonOuter(object):
    
    class __SingletonInner(object):
        
        def __init__(self, arg):
            self.arg = arg
        
        def __str__(self):
            return repr(self) + self.arg
        
    instance = None
    
    def __init__(self, arg):
        if not SingletonOuter.instance:
            SingletonOuter.instance = SingletonOuter.__SingletonInner(arg)
            print('First initialization')
        else:
            SingletonOuter.instance.arg = arg
            print('Duplicate initialization')
                    

if __name__ == '__main__':
    x = SingletonOuter('Sameer')
    print('x = {}'.format(x))
    print('x.instance = {}'.format(x.instance))
    y = SingletonOuter('Arnab')
    print('y = {}'.format(y))
    print('y.instance = {}'.format(y.instance))
    z = SingletonOuter('Umesh')
    print('z = {}'.format(z))
    print('z.instance = {}'.format(z.instance))
    print('x = {}'.format(x))
    print('x.instance = {}'.format(x.instance))
    print('y = {}'.format(y))
    print('y.instance = {}'.format(y.instance))
    