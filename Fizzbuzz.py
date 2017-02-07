#division game where any number divisible by 3 is replaced by "fizz" while any number divisible by 5 is replaced with "buzz"
for z in range (1, 101):#specify the range
	if z%3==0 and z%5==0:
		print "FizzBuzz"
	if z% 3==0 and z%5 !=0:
		print "Fizz"
	elif z%5==0 and z%3 !=0:
		print "Buzz"
	else:
		print z

