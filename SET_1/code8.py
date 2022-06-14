from Crypto.Cipher.AES import block_size

def count_blocks(text):
	blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
	nduplicates = len(blocks) - len(set(blocks)) # finding the number of duplicates by subtracting unique blocks from total
	return nduplicates
	
def solve(filename):
	message = [bytes.fromhex(text.strip()) for text in open(filename)]

	score = (-1, 0) # index of line and number of duplicate blocks 	
	for index, val in enumerate(message):
		duplicates = count_blocks(val)
		score = max(score, (index, duplicates), key=lambda t: t[1])
	return score
	
if __name__ == '__main__':
	index, dupl = solve('8.txt')
	print("Line number: ", index)
	print("Number of Duplicate Blocks: ", dupl) 
