import bz2

unbz=bz2.BZ2File("plotMe.xml.bz2").read()
print unbz	#get content of bz file

text = " hi, this is a test"
bzcompress=bz2.compress(text)
print bzcompress

f = open("test.bz","w")
f.write(bzcompress)
f.close()

