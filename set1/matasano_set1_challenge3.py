import matasano_set1_challenge1 as m11
import matasano_set1_challenge2 as m12

###################################
# Challenge 3 - Single-byte XOR cipher
# The hex encoded string:

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

#x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# From http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}


def max_score(stuff): 
    score = 0
    for i in stuff:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score

def strxor(stuff, key_byte): 
    print stuff, key_byte
    return [(stuff[i])^key_byte for i in range(len(stuff))]


def reverse_single_xor(stuff):
    def key(p):
        return max_score(p)

    result= max([strxor(stuff, i) for i in range(0, 256)], key=key)
    #print "".join(chr(result[i]) for i in range(len(result)))
    return result

reverse_single_xor(m11.hex2ascii('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))

