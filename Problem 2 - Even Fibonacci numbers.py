num1 = 1
num2 = 2
num3 = 0
sumFib = num2

while num3 < 4000000:
	if num3 % 2 == 0:
		sumFib += num3

	num3 = num1 + num2
	num1 = num2
	num2 = num3

print sumFib

