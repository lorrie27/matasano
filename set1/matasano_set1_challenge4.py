import matasano_set1_challenge1 as m11
import matasano_set1_challenge2 as m12
import matasano_set1_challenge3 as m13

file = '4.txt'

# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR.

# Find it.

# (Your code from #3 should help.)

def read_file(file):


	with open(file) as f:
		lines = [line.rstrip('\n') for line in f]

	return lines


def return_all_max(file): 

	strings = []
	line_numbers = []
	test_score = []


	for i,j in enumerate(read_file(file)):
		strings.append(m13.reverse_single_xor(m11.hex2ascii(j)))
		line_numbers.append(i)

	def score(i): 
		test_score.append(m13.max_score(strings[i]))
		return m13.max_score(strings[i])

	maxI = max(range(len(strings)), key=score)
	# print maxI
	# print strings[maxI]
	# print test_score[maxI]
	# print max(test_score)

	return (maxI, strings[maxI])

def select_line(string): 
	print "".join(chr(string[i]) for i in range(len(string)))

#select_line(return_all_max(file)[1])

