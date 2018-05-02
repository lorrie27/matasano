import matasano_set1_challenge1 as m11
import matasano_set1_challenge2 as m12
import matasano_set1_challenge3 as m13
import matasano_set1_challenge4 as m14

print 'Challenge 1: '
one = m11.hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
print "".join(str(i) for i in one).decode('base64')


print '\nChallenge 2: '
m12.fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')

print '\nChallenge 3: '
result = m13.reverse_single_xor(m11.hex2ascii('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
print "".join(chr(result[i]) for i in range(len(result)))


print '\nChallenge 4: '
stuff = m14.return_all_max('4.txt')
m14.select_line(stuff[1])

print '\nChallenge 5: '



