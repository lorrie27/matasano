string_codes = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="


#############################################
#	Challenge 1 - Convert hex to base64
# The string:

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:

# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

def hex2raw(blah):

	"""Return raw bytes from a hexadecimal string."""

	return blah.decode('hex')

def raw2hex(blah): 

	return blah.encode('hex')

def hex2ascii(in_list):

	#return x.decode('hex').encode('base64')

	ascii_list = []

	for i in range(0, len(in_list), 2):
		ascii_list.append(int(in_list[i]+in_list[i+1], 16))

	return ascii_list



def ascii2binary(in_list):

	digits = []
	k = in_list
	while k/2 !=0:
		digits.append(k % 2)
		k = k/2 

	digits.append(k%2)

	while len(digits)!=8:
		digits.append(0)

	digits.reverse()

	return digits


def binary2base64(in_list): 

	in_list.reverse()

	base_list = [i*(2**(j)) for j,i in enumerate(in_list)]
	base = sum(base_list)

	return base


def hex2base64(in_list):

	ascii_list = hex2ascii(in_list)

	binary_list = []

	for i in ascii_list:
		binary_list.append(ascii2binary(i))

	binary_list = sum(binary_list, [])

	while len(binary_list) % 3 !=0: 
		binary_list.append(0)

	new_binary_list_six = [binary_list[i:i+6] for i in range(0, len(binary_list), 6)]

	new_binary_list_base_ten = [binary2base64(i) for i in new_binary_list_six]

	base_list = [string_codes[i] for i in new_binary_list_base_ten]

	# print ascii_list
	# print binary_list
	# print new_binary_list_six
	# print new_binary_list_base_ten
	# print base_list
	k =  "".join(str(i) for i in base_list)
	#print k.decode('base64')
	return "".join(str(i) for i in base_list)

#hex2base64(x)