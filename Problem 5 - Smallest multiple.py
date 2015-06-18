def isMultiple(num, factor):
	if factor == 1:
		return True

	if num % factor == 0:
		return isMultiple(num, factor - 1)
	else:
		return False


max_check = 1000000000
highest_multiple = 20
for i in xrange (highest_multiple, max_check, highest_multiple):
	if isMultiple(i, highest_multiple - 1):
		print i
		break