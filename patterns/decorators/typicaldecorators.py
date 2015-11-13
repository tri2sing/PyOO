def decorator_func(to_be_decorated_func):
    ''' Input parameter is a function, return result is a function.
    '''
    def decorated_func(*args, **kwargs):
        print('Before {0}'.format(to_be_decorated_func.__name__))
        result = to_be_decorated_func(*args, **kwargs)
        print('After {0}'.format(to_be_decorated_func.__name__))
        return result
    decorated_func.__doc__ = to_be_decorated_func.__doc__
    decorated_func.__name__ = to_be_decorated_func.__name__
    return decorated_func

def hello():
    print('\tHello  called function')
    

print(32*'=')
print('Original hello name = {0}'.format(hello.__name__))
print('Calling original function')
hello()

# Method 1 of invoking a decorated_func : Redefine function
hello = decorator_func(hello)
print(32*'=')
print('Modified hello name = {0}'.format(hello.__name__))
print('Calling modified version')
hello()

# Method 2 of invoking a decorated_func: Syntactic sugar
# This saves the statement namaste = decorator_func(namaste)
# You lose access to the unmodified version.
@decorator_func
def namaste():
    print('\tNamaste from called function')
    
print(32*'=')
namaste()

# Using the same decorator with an input function that takes parameters
@decorator_func
def adder(x, y):
    return x + y

print(32*'=')
print (adder(3, 5))


def decorator_parameterizer(input_param):
    def param_decorator_func(input_func):
        def param_decorated_func(*args, **kwargs):
            result = input_func(*args, **kwargs)
            return result[:input_param]
        return param_decorated_func
    return param_decorator_func
        
# Method 1 of invoking a parameterized decorator
def data6alt():
    return "This is a really long string"

print(32*'=')
data6alt = decorator_parameterizer(6)(data6alt)
print(data6alt())
    
# Method 2 of parameterized decorator
@decorator_parameterizer(6)
def data6():
    return "This is a really long string"

print(32*'=')
print(data6())

@decorator_parameterizer(10)
def data10():
    return "This is a really long string"

print(32*'=')
print(data10())

