from base64 import b64decode
from code3 import *

def hamming(str1, str2):
	count = 0

	for i, j in zip(str1, str2):
		x = f'{ord(i):08b}'
		y = f'{ord(j):08b}'

		for a, b in zip(x,y):
			if a != b:
				count += 1

	return count

def readFile(filename):
	s1 = ""
	with open(filename) as f:
	    s1 += f.read().replace('\n', '')

	return b64decode(s1.encode())
	
def repeat_key_xor(string, key):
	message = ""
	
	for index, val in enumerate(list(string)):
		message += chr(val ^ ord(key[index % len(key)]))
	
	return message

def solve(filename):
	text = readFile(filename)
	min_score, size = 100.0, 0
	for keysize in range(2, 40):
		block1 = text[:keysize*8].decode()
		block2 = text[keysize*8:keysize*8*2].decode()
		
		score = hamming(block1, block2) / keysize
		if score < min_score:
			min_score = score
			size = keysize
	
	# we now have the size of the block, hopefully (emphasis on hopefully)
	blocks = list()
	for i in range(0, size):
		# we need to make size times blocks
		nth_block = bytes()
		for j in range(i, len(text), size):
			nth_block += text[j:j+1]
		blocks.append(nth_block)
		
	key = ""
	for block in blocks:
		temp_key, min_score, decoded_string = single_byte_xor(block)
		key += chr(temp_key)
		
	message = repeat_key_xor(text, key)
	
	return key, message
	
if __name__ == '__main__':
	key, text = solve('6.txt')
	print("KEY:\t", key, "\n\n")
	print("MESSAGE:\n\n", text)
