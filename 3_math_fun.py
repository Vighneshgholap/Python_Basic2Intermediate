#here we will learn more about the math function math()
#------------------------------------------------------------------------------------

# we have to import the library
import math

pi = 3.14
print(round(pi))            # rounds up according to the decimal : <= 3.49 -> 3 && >= 3.5 -> 4
#------------------------------------------------------------------------------------

print(math.ceil(pi))        # rounds up to the greatest value: 3.1 -> 4
print(math.floor(pi))       # rounds up to the lowest value: 3.9 -> 3
#------------------------------------------------------------------------------------

print(abs(pi))              # converts any number to positive number - becomes + 
print(pow(pi, 2))           # this is a^b: insert two num a and b. pi ^ 2 = 9.85
print(math.sqrt(pi))        # this function gives us the squareroot of a number (NO NEGATIVES ALLOWED) 
#------------------------------------------------------------------------------------

x = 1
y = 2
z = 3

print(max(x, y, z))         # to find the maximum value of the given variables
print(min(x, y, z))         # to find the minimum value of the given variables
#------------------------------------------------------------------------------------