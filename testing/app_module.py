'''
Created on Dec 6, 2015

@author: Sameer Adhikari
'''

def combine_character(plain, keyword):
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cipher, keyword):
    cipher = cipher.upper()
    keyword = keyword.upper()
    cipher_num = ord(cipher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cipher_num - keyword_num) % 26)


class VigenereCipher(object):
    def __init__(self, keyword):
        self.keyword = keyword
        
    def extend_keyword(self, num):
        repeats = num // len(self.keyword) + 1
        return (self.keyword * repeats)[:num]
    
    def _code_or_decode(self, text, combine_or_separate_func):
        text = text.replace(" ", "").upper()
        result = []
        keyword = self.extend_keyword(len(text))
        for p,k in zip(text, keyword):
            result.append(combine_or_separate_func(p,k))
        return "".join(result)

    def encode(self, plaintext):
        return self._code_or_decode(plaintext, combine_character)
    
    def decode(self, ciphertext):
        return self._code_or_decode(ciphertext, separate_character)
    
    