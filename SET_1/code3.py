from collections import Counter
import matplotlib.pyplot as plt

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def plot_linears(dist_1, dist_2, title=None):
    plt.plot(list(string.ascii_lowercase), dist_1, label="Standard Distribution")
    plt.plot(list(string.ascii_lowercase), dist_2, label="Text Distriution")
    plt.xlabel('Letters')
    plt.ylabel('Frequency (%)')
    plt.title(title)
    plt.legend()
    plt.show()
    
def score(text):
    freq_eng = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
    }
    counter = Counter(text)
    text_eng = [ (counter.get(i, 0) * 100) / len(text) for i in freq_eng]
    
    return sum([abs(i-j) for i, j in zip(list(freq_eng.values()), text_eng)]) / len(text)
    
def single_byte_xor(hex1):
    min_score = None
    decoded_string = ""
    key = 0
    for i in range(0, 256):
        temp_string = ""
        for j in list(hex1):
            temp_string += chr(i ^ j)
        temp_score = score(temp_string)
        if min_score is None or temp_score < min_score:
            min_score = temp_score
            decoded_string = temp_string
            key = i
    return (key, min_score, decoded_string)
    
if __name__ == '__main__':
    key, min_score, decoded_string = single_byte_xor(bytes.fromhex(hex_string))
    print("SCORE: ", min_score, "\nKEY: ", key, "\nDECODED STRING: ", decoded_string)
