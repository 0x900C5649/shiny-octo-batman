#! /usr/local/bin/pythonw
import sys
import hashlib
import os.path

dat1 = sys.argv[1]
dat2 = sys.argv[2]

def md5Checksum(filePath):
	if not os.path.exists(filePath):
		return '0'
	with open(filePath, 'rb') as fh:
		m = hashlib.md5()
		while True:
			data = fh.read(8192)
			if not data:
				break
			m.update(data)
		return m.hexdigest()

h1 = int(md5Checksum(dat1), 16)
h2 = int(md5Checksum(dat2), 16)
print (hex(h1 ^ h2))
