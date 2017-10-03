prime = [2,3,5,7,11,13,17,19]

count = len(prime)
for i in range(23,10000000,2):
	flag = True
	for j in prime:
		if i % j == 0:
			flag = False 
			break
		elif i < j*j:
			break
	if flag:
		prime.append(i)
print prime
