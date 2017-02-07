#division game where any number divisible by 3 is replaced by "fizz" while any number divisible by 5 is replaced with "buzz"
def fizz_buzz(number):
#specify the range
    if number%3==0 and number%5==0:
        print "FizzBuzz"
    if number% 3==0 and number%5 !=0:
        print "Fizz"
    elif number%5==0 and number%3 !=0:
        print "Buzz"
    else:
        print number