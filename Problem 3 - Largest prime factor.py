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

def primeFactors(num):
	if isPrime(num):
		return num
	i = 2
	while i < num:
		if num % i == 0:
			if isPrime(i):
				return i, primeFactors(num/i)
		i += 1


print primeFactors(600851475143)



