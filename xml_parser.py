import xml.etree.ElementTree as ET
import Tkinter

window = Tkinter.Tk()
cv = Tkinter.Canvas(window,width=1000,height=600)

tree = ET.parse('plotMe.xml')
root = tree.getroot()
#cv.create_line(0,0,100,100,fill="red")
#cv.create_line(0,0,100,110,fill="green")]
#cv.create_arc(200,200,400,400,start=180,extent=350,width=2.0,outline="blue",style="arc")
for child in root:
	shape = child.tag
	color = 'white'
	if shape == 'Line':
		for i in child:
			if i.tag == 'YEnd':
				yend = float(i.text)
			elif i.tag == 'YStart':	
				ystart = float(i.text)
			elif i.tag == 'XEnd':
				xend = float(i.text)
			elif i.tag == 'XStart':
				xstart = float(i.text)
			elif i.tag == 'Color':
				color = i.text
		cv.create_line(xstart,ystart,xend,yend,fill=color,width=2.0)
		#print 'line start({0},{1}) end({2},{3}) color:{4}'.format(xstart,ystart,xend,yend,color)
	elif shape == 'Arc':
		for i in child:
			if i.tag == 'Color':
				color = i.text
			elif i.tag == 'ArcExtend':	
				arcext = float(i.text)
			elif i.tag == 'ArcStart':
				arcstart = float(i.text)
			elif i.tag == 'XCenter':
				xcenter = float(i.text)
			elif i.tag == 'YCenter':
				ycenter = float(i.text)
			elif i.tag == 'Radius':
				radius = float(i.text)
			else:
				print "unexpected tag in LINE!!"+i.tag
		cv.create_arc(xcenter-radius,ycenter-radius,xcenter+radius,ycenter+radius,start=arcstart,extent=arcext,outline=color,width=2.0,style="arc")
cv.pack()
window.mainloop()