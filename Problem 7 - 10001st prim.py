import math

def isPrime(num):

	if num < 4:
		return True
	else:
		i = 2
		while i <= math.sqrt(num):
			if num % i == 0:
				return False
			i += 1

	return True

count = 1
for i in xrange(3,10000000,2):
	if isPrime(i):
		# print i
		count +=1
		if count == 10001:
			print 'The ' + str(count) + 'st prime is: ' + str(i)
			break

print count