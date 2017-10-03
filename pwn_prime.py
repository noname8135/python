prime = [2,3,5,7,11,13,17,19]

count = len(prime)
ans = []
for i in range(23,1100000,2):
	flag = True
	for j in prime:
		if i % j == 0:
			flag = False 
			break
		elif i < j*j:
			break
	if flag:
		prime.append(i)

for i in prime:
	if i > 1000000:
		a=[int(j) for j in str(i)]
		a_sum = sum(a)
		if a_sum in prime:
			ans.append(i)
	if len(ans) == 2 :
		break
print ans
