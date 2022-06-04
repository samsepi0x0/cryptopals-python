def repeat_key_xor(S, K):
	final_msg = ""
	for i in range(len(S)):
		final_msg += chr(ord(S[i]) ^ ord(K[i % len(K)]))
	
	return bytes.hex(bytes(final_msg.encode('utf-8')))

if __name__ == '__main__':
	string_1 = input("TEXT: ")
	key = input("KEY: ")
	
	hex1 = repeat_key_xor(string_1, key)
	
	print("\nEncoded text: \n", hex1)
