from Crypto.Cipher import AES
from base64 import b64decode

def readFile(filename):
    text = ""
    with open(filename, 'r') as f:
        text += f.read().replace('\n', '')
    return b64decode(text)

def solve(filename, key):
    '''
    	Python ECB mode decipher automatically splits text into blocks of 16 and applies key to it, in another language, maybe text needs to be split manually before decrypting
    '''
    if len(key) != 16:
        print("Key length should be 16 Bytes.")
        return -1
    text = readFile(filename)

    decipher = AES.new(key, AES.MODE_ECB)

    return decipher.decrypt(text).decode('utf-8')

if __name__ == '__main__':
    result = solve("7.txt", b'YELLOW SUBMARINE')
    print(result)
