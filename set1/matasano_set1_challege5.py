import matasano_set1_challenge1 as m11
#import matasano_set1_challenge2 as m12
#import matasano_set1_challenge3 as m13
#import matasano_set1_challenge4 as m14

import string
import itertools as it

# Implement repeating-key XOR
# Here is the opening stanza of an important work of the English language:

# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal
# Encrypt it, under the key "ICE", using repeating-key XOR.

# In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

# It should come out to:

# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
# Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.

match1 = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

def ascii_to_hex(a): 

	return a.encode('hex')

def encode_text(keyword, stuff): 

	stuff_hex = [m11.hex2ascii(ascii_to_hex(i))[0] for i in stuff]
	keyword_hex = [m11.hex2ascii(ascii_to_hex(i))[0] for i in keyword]

	output=[ord(j)^ord(keyword[i % len(keyword)]) for (i,j) in enumerate(stuff)]

	result = [(ascii_to_hex(chr(i))) for i in output]
	y =  "".join(result)
	print y
	return y
