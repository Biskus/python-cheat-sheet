import hashlib
from pprint import pprint as p

def md5(string):
    return hashlib.md5(word.encode()).hexdigest()

def sha256(string):
    return hashlib.sha256(string.encode()).hexdigest()

def sha512(string):
    return hashlib.sha512(string.encode()).hexdigest()

def sha3_256(string):
    return hashlib.sha3_256(string.encode()).hexdigest()

def sha3_512(string):
    return hashlib.sha3_512(string.encode()).hexdigest()



def encrypt_word(string):
    print(f'MD5: {md5(string)}')
    print(f'SHA2-256: {sha256(string)}')
    print(f'SHA2-512: {sha512(string)}')
    print(f'SHA3-256 {sha3_256(string)}')
    print(f'SHA3-512 {sha3_512(string)}')


word = 'arvid'   
encrypt_word(word)



