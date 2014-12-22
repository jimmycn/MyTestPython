#! /usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get filename
while  True:
if os.path.exists(fname):
	print("Error")
else:
	break
all = []
print("enter lines")

while True:
	entry=input('>')
	if entry== '.':
		break
	else:
		all.append(entry)
fobj=open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('Done')
	
