import binascii
import sys

searchFor = "e0"

offset = 0
lastOffset = 0
fileName = sys.argv[1]

with open(fileName, "rb") as f:
	byte = f.read(1)
	while byte != "":		
		if binascii.hexlify(byte) == searchFor:
			distance = offset - lastOffset
			print "Delimiter at " + str(lastOffset) + " dec. dist=" + str(distance)
			lastOffset = offset
		else:
			offset += 1
		byte = f.read(1)