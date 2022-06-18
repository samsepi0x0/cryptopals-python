# cryptopals-python
A collection of python codes for the [cryptopals series.](https://cryptopals.com/)

## Description:
  This repo contains the collection of all the python codes (along with the text files provided in the question) I wrote to solve the cryptopals series.
  Now that SET 1 is complete, I will be starting SET 2 soon. The file structure will update according to the status of the challenges solved.
  
  
### SET 1:
This is the qualifying set. We picked the exercises in it to ramp developers up gradually into coding cryptography, but also to verify that we were working with people who were ready to write code.

This set is relatively easy. With one exception, most of these exercises should take only a couple minutes. But don't beat yourself up if it takes longer than that. It took Alex two weeks to get through the set!

If you've written any crypto code in the past, you're going to feel like skipping a lot of this. Don't skip them. At least two of them (we won't say which) are important stepping stones to later attacks. 

  | S.No | Name | Links |
  |:---|:------------------------------:|----------:|
  | 1.| Convert hex to base64 | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code1.py) |
  | 2.| Fixed XOR | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code2.py) |
  | 3.| Single-byte XOR cipher | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code3.py) |
  | 4.| Detect single-character XOR | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code4.py), [TXT](https://github.co/samsepi0x0/cryptopals-python/blob/main/SET_1/4.txt) |
  | 5.| Implement repeating-key XOR | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code5.py) |
  | 6.| Break repeating-key XOR | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code6.py), [TXT](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/6.txt) |
  | 7.| AES in ECB mode | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code7.py), [TXT](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/7.txt) |
  | 8.| Detect AES in ECB mode | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/code8.py), [TXT](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_1/8.txt) |


### SET 2:
 This is the first of several sets on block cipher cryptography. This is bread-and-butter crypto, the kind you'll see implemented in most web software that does crypto.

This set is relatively easy. People that clear set 1 tend to clear set 2 somewhat quickly.

Three of the challenges in this set are extremely valuable in breaking real-world crypto; one allows you to decrypt messages encrypted in the default mode of AES, and the other two allow you to rewrite messages encrypted in the most popular modes of AES. 

  | S.No | Name | Links |
  |:---|:------------------------------:|----------:|
  | 9. | Implement PKCS#7 padding | [Link](https://github.com/samsepi0x0/cryptopals-python/blob/main/SET_2/code9.py) |
