import argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-e", "--encrypt", action="store_true", help="encrypt the input file")
	group.add_argument("-d", "--decrypt", action="store_true", help="decrypt the input file")
	parser.add_argument("-o", "--outfile", help="the output file (stdout by default if missing)")
	parser.add_argument("-k", "--key", help="the key value")
	parser.add_argument("infile", help="input file")	
	args = parser.parse_args()