'''Fiiiiizzzzzz Buuuuuuzzzzzzzz Algorithm
   Made by Callum for the Python Programming Society
   Introducing libraries and loops
'''

import time

number = 1

while number <= 30:
    if number % 3 == 0 and number % 5 == 0:
        print(str(number) + ' - Fizzbuzz')
    elif number % 5 == 0:
        print(str(number) + ' - Buzz')
    elif number % 3 == 0:
        print(str(number) + ' - Fizz')
    else:
        print(str(number))
    number += 1
    time.sleep(1)
