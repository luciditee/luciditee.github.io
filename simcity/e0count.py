import binascii
import sys

searchFor = "e0"

offset = -1
lastOffset = 0
fileName = sys.argv[1]

with open(fileName, "rb") as f:
	byte = f.read(1)
	while byte != "":
		offset += 1	
		
		if binascii.hexlify(byte) == searchFor:
			distance = offset - lastOffset
			print "Delimiter at " + str(offset) + " dist=" + str(distance)
			lastOffset = offset
			
		byte = f.read(1)
