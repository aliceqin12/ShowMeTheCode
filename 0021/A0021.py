import os
import hashlib

def encrypt_password(password, salt=None):
    if salt == None:
        salt = os.urandom(8)
        print(salt)

    result = password
    for i in range(10):
        result = hashlib.pbkdf2_hmac(hash_name='sha256',
                                     password=password,
                                     salt=salt,
                                     iterations=100000)

    return (result, salt)

if __name__ == '__main__':
    (result, salt) = encrypt_password(b'zay1231232567')
    print(result)
    print(salt)