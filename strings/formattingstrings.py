'''
Created on Dec 3, 2015

@author: Sameer Adhikari
'''

# creating hard coded strings

a = 'hello' # using single quote
b = "hello" # using double quote
c = '''first multi
line '''
print(c)
d = """second multi
line str"""
print(d)
e = 'auto concat: ' 'hi ' 'there! ' 'it is me.' 
# This is equal to e = 'auto concat: hit there! it is me.'  
# Interpreter automatically concatenates.
print(e)

# Using positional arguments with the format method
template = "Hello {}, you are currently {}."
print(template.format('Dusty', 'writing'))

# Using numbered arguments with the format method
template = "Hello {0}, you are {1}. Your name is {0}."
print(template.format('Dusty', 'writing'))

# Using keyword arguments with the format method
template = "Hello {name}, you are currently {doing}."
print(template.format(doing='writing', name='Dusty'))

# Using container lookups with the format method
emails1 = ("a1@example.com", "b1@example.com")
emails2 = ["a2@example.com", "b2@example.com"]
message = {
        'subject': "You Have Mail!",
        'message': "Here's some mail for you!"
        }
template = """
From: <{0[0]}>
To: <{1[1]}>
Subject: {message[subject]}
{message[message]}"""
print(template.format(emails1, emails2, message=message))
# Note that the string keys used in the dictionary lookup are not quoted.

# Using object attributes (dot notation) with the format method.
class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email = EMail("a@example.com", "b@example.com",
        "You Have Mail!",
         "Here's some mail for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}
{0.message}"""
print(template.format(email))
print()


orders = [('burger', 2, 5),
        ('fries', 3.5, 1),
        ('cola', 1.75, 3)]
print("PRODUCT    QUANTITY    PRICE    SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print("{0:10s} {1: ^9d} ${2: <8.2f} ${3: >7.2f}".format(product, quantity, price, subtotal))
    

# Escaping braces
# Simplest Python program, which prints the simplest Java program, which prints the simplest Python program
print()
template = """
public class {0} {{
    public static void main(String[] args) {{
        System.out.println("{1}");
    }}
}}"""

print(template.format("MyClass", "print('hello world')"));    



