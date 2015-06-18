def isPalindrome(numString):
	if numString == '':
		return True

	if numString[0] == numString[-1]:
		return isPalindrome(numString[1:len(numString) - 1])
	else:
		return False


largest = 0
product = 0

for x in range(100,999):
	for y in range(100,999):
		product = x * y
		if isPalindrome(str(product)):
			largest = max(product, largest)

print largest