while True:
	try:
		x = raw_input()
		print x
	except Exception as ex:
		template = "An exception of type {0} occured. Arguments:\n{1!r}"
		message = template.format(type(ex).__name__, ex.args)
		print message
		#use pass to ignore items
	finally:	#do clean up before exiting
		