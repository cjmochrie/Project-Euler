a = 0
b = 0
c = 0

for a in xrange(1,1000):
	for b in xrange(1, 1000 - a):
		c = 1000 - a -b
		sum = a*a + b*b
		if c*c == sum:
			print 'a: ' + str(a)
			print 'b: ' + str(b)
			print 'c: ' + str(c)
			print a*b*c
			break

