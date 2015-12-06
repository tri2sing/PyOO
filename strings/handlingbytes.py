'''
Created on Dec 3, 2015

@author: Sameer Adhikari
'''

# Converting bytes to text
characters = b'\x63\x6c\x69\x63\x68\xe9'
string = " ".join(['x%0x' %c for c in characters])
print(string)
print('displaying as ascii = {}'.format(characters))
print('displaying as latin-1 = {}'.format(characters.decode("latin-1")))

# Converting text to bytes
# DThe accented character is represented differently for each encoding.
# And, in the case of ascii, we cannot even encode it 
characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
try:
    print(characters.encode("ascii"))
except UnicodeEncodeError:
    print('Unable to encode in ascii')


