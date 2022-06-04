import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex2b64(hex_str):
    '''
        use b64encode to encode the bytes.fromhex(the hex string) and decode
        the whole to utf-8 to make it a string.
    '''
    return base64.b64encode(bytes.fromhex(hex_string)).decode('utf-8')

if __name__ == '__main__':
    test_string = hex2b64(hex_string)
    final_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print("%s == %s : %r" % (test_string, final_string, test_string == final_string))
