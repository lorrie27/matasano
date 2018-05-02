import matasano_set1_challenge1 as m11

############################################################
#	Challenge 2 - Fixed XOR

# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965
# ... should produce:

# 746865206b696420646f6e277420706c6179

#convert = '1c0111001f010100061a024b53535009181c' 
#cross = '686974207468652062756c6c277320657965'

def fixed_xor(convert, cross):

	if len(convert) != len(cross):
		return None

	convert_decode = m11.hex2raw(convert)
	cross_decode = m11.hex2raw(cross)

	#print convert_decode
	print cross_decode

	fixed =([chr(ord(i)^ord(j)) for (i,j) in zip(convert_decode, cross_decode)])
	fixed= "".join(fixed)
	print fixed
	# print fixed.encode('hex')
	return m11.raw2hex(fixed)


#fixed_xor(convert, cross)