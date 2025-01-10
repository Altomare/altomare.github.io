with open('BIOS25.ASM', 'rb') as BIOS25:
	with open('BIOS25_CLEANED.ASM', 'w+b') as cleaned:
		c = BIOS25.read(1)
		# print(c)
		while (c):
			if (c[0] & 0x80):
				print(bytes([c[0] & 0x7f]))
				cleaned.write(bytes([c[0] & 0x7F]))
			else:
				cleaned.write(c)
			c = BIOS25.read(1)
