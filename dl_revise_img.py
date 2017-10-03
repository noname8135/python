import Image
import requests
import string
import pytesseract
import subprocess
"""
img = requests.post('http://securityoverride.org/challenges/programming/11/php_captcha.php',cookies={'PHPSESSID':"8b9dce298e23f1293b7f5288055f2ae0"});
f = open("./.jpg",'w')
f.write(img.content)
f.close()
"""


def process_img(ori):
	width,height = ori.size[0], ori.size[1]
	# change collor
	"""
	for i in range(0,height):
		for j in range(0,width):
			#print ori.getpixel((j,i)),
			r,g,b = ori.getpixel((j,i))
			if (r,g,b) < (100,100,100):
				r,g,b = (0,0,0)
			
			ori.putpixel((j,i),(255-r,255-g,255-b))
	"""
	print ori.size
	ori = ori.resize((1000,50))
	ori.save("new.jpg")
	
if __name__ == '__main__':
	img = Image.open("gimme.jpg")
	process_img(img)
	subprocess.call(["tesseract","new.jpg","output","nobatch","my_char_list"])
	aaa = open("output.txt")
	print aaa.read()
	sys.exit
	result = ''
	for i in aaa.readline():
		if i != ' ':
			result += i
	print result
	#print pytesseract.image_to_string(Image.open('new.jpg'))