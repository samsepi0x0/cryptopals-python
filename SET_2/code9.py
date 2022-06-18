def pkcs_padding(message, length=16, byte=b'\x04'): # returns byte string, decode() to convert to string
	if len(message) % length == 0:
		return message
	msg = bytes(message.encode())
	for i in range(len(message), length):
		msg += byte
	return msg

if __name__ == '__main__':
	padded_text = pkcs_padding("YELLOW SUBMARINE", 20)
	print("Padded text: ", padded_text, len(padded_text))
	print(padded_text.decode() == "YELLOW SUBMARINE\x04\x04\x04\x04")
