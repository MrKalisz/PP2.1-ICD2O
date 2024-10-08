'''
    Lesson: 1.10 - Math Library
    Author: Mr. Kalisz
    Date Created: Oct 2, 2024
    Date Last Modified: Oct 2, 2024
'''

#import - this has to be before all your code

import math

#ceil -> ceiling - rounds a value up 

num = 3.5

print(math.ceil(num)) #Function.  math is just where the function is located

#floor

num = 3.5

print(math.floor(num))

#isqrt - integer square root - only works on integers
#Gives an integer as a result

num = 9

print(math.isqrt(num))

#sqrt - square root - works on any number
#always gives a float as a result

num = 9

print(math.sqrt(num))

#trunc - truncate - process of removing something from the end

num = -3.5

print(math.trunc(num)) #rounds towards zero by removing the decimal point
print(int(num)) #does the same as trunc
print(math.floor(num)) #rounds down
print(math.ceil(num)) #rounds up

#Many more - https://docs.python.org/3/library/math.html