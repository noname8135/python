import time

# Record start time
tStart = time.time()

for i in range(0,2047483644):
	if i%10000==0:
		print i

# Record stop time
tStop = time.time()
print(tStop - tStart)
