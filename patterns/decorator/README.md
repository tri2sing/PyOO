Right Way to Explain Decorators
* A function is an object that generates a value based on the values of its arguments.
* In Python, functions are first-class objects, so they can be passed around like other objects (strings, integers, etc.).
* Hence, we can write functions that both (a) accept function objects as argument values, and (b) return function objects as return values.
* A decorator is a function that takes a function as an argument, and returns a function as a return value.
* The power of a decorator is that it can use the function passed in as argument, to help in the creation of the function that it returns.
* To invoke a decorator, we call it with a function argument, and get back another function as the return value.
* Decorators are often used to create a new function that does what the original function does, but also some additional things.
* Python provides syntactic sugar (@ followed by a decorator name), that is, a decoration line.  It is a shortcut to handling function variable assignments.

Credits: https://pythonconquerstheuniverse.wordpress.com/2012/04/29/python-decorators/

