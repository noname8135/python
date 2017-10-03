import sys
import random
import gmpy

def get_prime(size):
	while True:
		val = prng.getrandbits(size)
		if gmpy.is_prime(val):
			return val

if __name__ == '__main__':
	get_prime(sys.argv[1])
