#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
	last = number % -10
else:
	last = number % 10

if last > 5:
	print('Last digit of', number, 'is', last, 'and greater than 5')
elif last == 0:
	print('Last digit of', number, 'is', last, 'and is 0')
else:
	print('Last digit of', number, 'is', last, 'and is less then 6 and not 0')
