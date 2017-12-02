stringdata = "http://www.pythonchallenge.com/pc/def/map.html"



chars = []

for ch in stringdata:
	if ch == "y":
		chars.append("a")
	elif ch == "z":
		chars.append("b")
	elif ch.isalpha():
		a = (ord(ch)+2%26)
		chars.append(chr(a))

	else:
		chars.append(ch)
print "".join(chars)




