import zipfile
import os
import subprocess
import tarfile
import gzip
import bz2
num = int(raw_input("num:"))
subname = raw_input("subname:")
fname = str(num)+subname
dir_name = ''

while num > 0:
	print "___"+fname+"____"
	full_name = dir_name + fname.replace('-','\-').replace('*','\*').replace('.','\.')
	#type_msg.split(" ")[1]
	type_msg = subprocess.check_output("file "+full_name,shell=True)
	end = type_msg.split(" ")[1]
	print "end = ",end
	if end == 'Zip':
		a = zipfile.ZipFile(dir_name+fname,'r')
		a.extractall()
	elif end == 'gzip':
		ungz = gzip.open(dir_name+fname).read()
		f = open("tmp","w")
		f.write(ungz)
		f.close()
		a = tarfile.open('tmp','r')
		a.extractall()
	elif end == 'bzip2':
		unbz=bz2.BZ2File(dir_name+fname).read()
		f = open("tmp","w")
		f.write(unbz)
		f.close()
		a = tarfile.open('tmp','r')
		a.extractall()
	else:
		print "special end!!__"+end+"__"
		sys.exit()
	num -= 1
	dir_name = str(num)+'/'
	indir=os.listdir(dir_name)
	fname = indir[len(indir)-1]
	

