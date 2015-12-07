'''
Created on Dec 6, 2015

@author: Sameer Adhikari
'''

# For test-driven development (TDD), write tests 
# before writing the methods in the app module.
# These tests are run using pytest in my environment

from testing.app_module import combine_character, \
    separate_character, VigenereCipher

def test_encode_string():
    cipher = VigenereCipher('TRAIN')
    encoded = cipher.encode('ENCODEDINPYTHON')
    assert encoded == 'XECWQXUIVCRKHWA'

def test_econde_character():
    cipher = VigenereCipher('TRAIN')
    encoded = cipher.encode('E')
    assert encoded == 'X'
    
def test_encode_spaces():
    '''Expected behavior of encoder is to remove the spaces in the input'''
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_lowercase():
    '''Expected behavior of the encode is to convert the input to all upper case'''
    cipher = VigenereCipher("TRain")
    encoded = cipher.encode("encoded in Python")
    assert encoded == "XECWQXUIVCRKHWA"

def test_combine_character():
    assert combine_character('E', 'T') == 'X'
    assert combine_character('N', 'R') == 'E'
    
def test_extend_keyword():
    cipher = VigenereCipher('TRAIN')
    extended = cipher.extend_keyword(16)
    assert extended == 'TRAINTRAINTRAINT'

def test_separate_character():
    assert separate_character("X", "T") == "E"
    assert separate_character("E", "R") == "N"

def test_decode():
    cipher = VigenereCipher("TRAIN")
    decoded = cipher.decode("XECWQXUIVCRKHWA")
    assert decoded == "ENCODEDINPYTHON"
