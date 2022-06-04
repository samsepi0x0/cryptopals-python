from code3 import *

def finding_xor(filename):
    files = open(filename, 'r')
    Key = 0
    minimum_score = None
    dec_string = ""
    while True:
        line = files.readline()
        if not line:
            break
        key, min_score, decoded_string = single_byte_xor(bytes.fromhex(line.strip()))
        if minimum_score is None or min_score < minimum_score:
            Key = key
            minimum_score = min_score
            dec_string = decoded_string
    return (Key, minimum_score, dec_string) 
        
if __name__ == '__main__':
    key, min_score, decoded_string = finding_xor('4.txt')
    print("\nSCORE: ", min_score, "\nKEY: ", key, "\nDECODED STRING: ", decoded_string)
