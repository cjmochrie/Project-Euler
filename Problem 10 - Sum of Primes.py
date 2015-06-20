import math

def isPrime(num):

	if num < 4:
		return True
	else:
		if num % 2 == 0:
			return False
		else:
			i = 3
			while i <= math.sqrt(num):
				if num % i == 0:
					return False
				i += 2

	return True

sum = 2
for i in xrange(3,2000000,2):
	if isPrime(i):
		sum += i

print sum