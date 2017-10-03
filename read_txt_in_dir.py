import os

indir = os.listdir('./')
for files in indir:
	if files.endswith('.txt'):
		txtfile = open('./'+files)
		content=txtfile.read()
		if content != 'Nothing here...':
			print "{0} contain:{1}___bingo".format(files,content)
