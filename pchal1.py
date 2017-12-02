#!/usr/bin/python
# k - m
# o - q
# e - g
# s - q shift by 2 letters mod 26

stringdata = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
chars = {}
i = 0
for ch in stringdata:
	chars[i] = chr(ord(ch)+2)
#	print ord(ch)
#	print chars[i]
	i = i + 1
st = ""
for c in chars:
#	print type(c)
	
	st = st + str(chars[c])

print st
#print chars

