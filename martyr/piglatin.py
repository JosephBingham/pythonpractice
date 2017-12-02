#!/usr/bin/python

def main():
	print "word to piglatin: "
	stringy = raw_input()
	wordy = stringy.split(" ")
	s = ""
	for i in xrange(len(wordy)):
		s += piglatin(wordy[i]) + " "
	print s


def piglatin(stringy):
	vowels = ['a', 'e', 'i', 'o', 'u']
	letters = list(stringy)
	letters.append("-")
	if letters[0] in vowels:
		letters.append("h")
	letters.append(letters[0])
	letters.append("a")
	letters.append("y")
	letters[0] = ""
	stringed = ""
	for s in letters:
		stringed += s
	return stringed

if __name__ == '__main__':
	main()

