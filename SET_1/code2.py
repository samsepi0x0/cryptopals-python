hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

def fixed_xor(hex1, hex2):
    '''
        Check string lengths, if equal, loop each char of string, convert to int, xor with same index char on next string, make the whole thing to hex and append to string without the initial 0x prefix.
    '''
    if(len(hex1) != len(hex2)):
        return "Different Lengths. Cannot Be Xored."
    hex3 = ""

    for i, j in zip(hex1, hex2):
        hex3 += str(hex(int(i,16) ^ int(j,16)))[2:]

    return hex3

if __name__ == '__main__':
    test_string = fixed_xor(hex_string1, hex_string2)
    final_string = "746865206b696420646f6e277420706c6179"
    print("%s == %s : %r" % (test_string, final_string, test_string == final_string))

