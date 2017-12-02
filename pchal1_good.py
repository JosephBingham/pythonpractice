#!/usr/bin/python
# k - m
# o - q
# e - g
# s - q shift by 2 letters mod 26

stringdata = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
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






