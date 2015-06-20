import math
from timed_function import timer


@timer
def sum_primes():
	primes =[2]
	sum = 2
	is_prime = True
	for i in xrange(3,2000000,2):
		sqrt_i = math.sqrt(i)
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
			if prime > sqrt_i:
				break
		if is_prime:
			primes.append(i)
			sum += i
		is_prime = True


	print sum
	#print primes

sum_primes()