import png

pic = png.Reader("PNG.png")
print pic.read()

front=0

pixel_ary=pic.read()[2]
moorse=''
walker=0
for row in pixel_ary:
	for col in row:
		if col == 1:
			moorse += chr(walker - front)
			front = walker
		walker += 1

moose_to_ascii={'.-':'A',
'-...':'B',
'-.-.':'C',
'-..':'D',
'.':'E',
'..-.':'F',
'--.':'G',
'....':'H',
'..':'I',
'.---':'J',
'-.-':'K',
'.-..':'L',
'--':'M',
'-.':'N',
'---':'O',
'.--.':'P',
'--.-':'Q',
'.-.':'R',
'...':'S',
'-':'T',
'..-':'U',
'...-':'V',
'.--':'W',
'-..-':'X',
'-.--':'Y',
'--..':'Z',
'.----':'1',
'..---':'2',
'...--':'3',
'....-':'4',
'.....':'5',
'-....':'6',
'--...':'7',
'---..':'8',
'----.':'9',
'-----':'0'}
word = ''
ans = ''
for i in moorse:
	if i == ' ':
		ans+=moose_to_ascii[word]
		word=''
	else:
		word+=i
print ans