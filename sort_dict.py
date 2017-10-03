def by_key(mydict):
	for key in sorted(mydict.iterkeys()):
		print "%s: %s" % (key, mydict[key])

def by_value(mydict):
	for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
		print type((key, value))


mydict = {
	'a':12,
	'd':-10,
	'c':6,
	'z':7,
	'b':5
}
by_value(mydict)
by_key(mydict)