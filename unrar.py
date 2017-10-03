import rarfile
import os

def recursive_unrar():
	unrared=[]
	flag = True
	while flag == True:
		flag = False
		indir=os.listdir('./')
		for files in indir:
			if rarfile.is_rarfile(files) and files not in unrared:
				flag = True
				unrared.append(files)
				extract=rarfile.RarFile(files)
				extract.extractall()

if __name__=='__main__':
	recursive_unrar()
