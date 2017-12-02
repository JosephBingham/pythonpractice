class seq():
	seqarr = ""
	def isValidLetter(self, ch):
		return(ch.isalpha())

	def __init__(self, seqarr):
		for ch in seqarr:
			if( not (self.isValidLetter(ch))):
				raise ValueError("illegal argument")
			else:
				self.seqarr = seqarr

	def seqLength(self):
		return len(seqarr)

	def getSeq(self):
		return seqarr

	def toString(self):
		stringy = ""
		for ch in seqarr:
			stringy += ch.upper()
		return stringy

	def equals(self, newObj):
		if(newObj is seq):
			return True
		elif (type(newObj).__name__ != type(self).__name__):
			return False
		elif (newObj.toString() == self.toString()):
			return True


class proteinseq(seq):
	def __init__(self, seqarr):
		super().__init__(seqarr)

	def isValidLetter(ch):
		ch = ch.upper()
		booleany = not ((ch == 'B') or (ch == 'J') or (ch == 'O') or (ch == 'U') or (ch == 'X') or (ch == 'Z'))
		return (super.isValidLetter(ch) and booleany)


class DNAseq(seq):
	def __init__(self, seqarr):
		super().__init__(seqarr)

	def isValidLetter(ch):
		ch = ch.upper()
		return((let=='A') or (let=='C') or (let=='G') or (let=='T'))


class CodingDNAseq(DNAseq):
	def __init__(self, seqarr):
		super().__init__(seqarr)

	def checkStartCodon(self):
		if(len(seqarr) < 3):
			return False
		else:
			return ((seqarr[0].upper() == 'A') and (seqarr[1].upper() == 'T') and (seqarr[2].upper() == 'G'))

	def translate(self):
		if(not self.checkStartCodon):
			raise RuntimeError("No Start Codon")
		else:
			maxNumberOfCodons = self.seqLength()/3
			for i in xrange(maxNumberOfCodons):
				n = i*3
				stringed = ""
				while(n<(i+1)*3):
					if(stringed.getAminoAcid() == '$'):
						break
					else:
						stringed += seqarr[n]
				if(stringed.getAminoAcid() == '$'):
					break
				else:
					 translated[i] = stringed.getAminoAcid
			return translated

	def getAminoAcid(codon):
		if ( not codon ):
			 return '$'
		else:
			return{
				"AAA": 'K',
				"AAC": 'N',
				"AAG": 'K',
				"AAT": 'N',
				"ACA": 'T',
				"ACC": 'T',
				"ACG": 'T',
				"ACT": 'T',
				"AGA": 'R',
				"AGC": 'S',
				"AGG": 'R',
				"AGT": 'S',
			        "ATA": 'I',
				"ATC": 'I',
	        		"ATG": 'M',
			        "ATT": 'I',
	       			"CAA": 'Q',
	       			"CAC": 'H',
			        "CAG": 'Q',
	     			"CAT": 'H',
			        "CCA": 'P',
			        "CCC": 'P',
			        "CCG": 'P',
			        "CCT": 'P',
 			        "CGA": 'R',
			        "CGC": 'R',
       				"CGG": 'R',
      			        "CGT": 'R',
			        "CTA": 'L',
			        "CTC": 'L',
       				"CTG": 'L',
      				"CTT": 'L',
			        "GAA": 'E',
		       		"GAC": 'D',
			        "GAG": 'E',
			        "GAT": 'D',
			        "GCA": 'A',
			        "GCC": 'A',
			        "GCG": 'A',
			        "GCT": 'A',
			        "GGA": 'G',
			        "GGC": 'G',
			        "GGG": 'G',
			        "GGT": 'G',
			        "GTA": 'V',
			        "GTC": 'V',
			        "GTG": 'V',
			        "GTT": 'V',
		        	"TAA": '$',
			        "TAC": 'Y',
			        "TAG": '$',
			        "TAT": 'Y',
	       	       		"TCA": 'S',
			        "TCC": 'S',
			        "TCG": 'S',
			        "TCT": 'S',
			        "TGA": '$',
			        "TGC": 'C',
			        "TGG": 'W',
			        "TGT": 'C',
		        	"TTA": 'L',
		                "TTC": 'F',
		                "TTG": 'L',
		                "TTT": 'F'}[codon]

def main():
	sequenced = seq(['A', 'T', 'G', 'C', 'C', 'C'])
	print sequenced.toString()


if __name__ == '__main__':
	main()









