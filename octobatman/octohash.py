#! /usr/local/bin/pythonw
import sys
import hashlib

dat1 = sys.argv[1]


def md5Checksum(filePath):
	with open(filePath, 'rb') as fh:
		m = hashlib.md5()
		while True:
			data = fh.read(8192)
			if not data:
				break
			m.update(data)
		return m.hexdigest()

h1 = int(md5Checksum(dat1), 16)
print (hex(h1))