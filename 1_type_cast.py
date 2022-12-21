#Converting a Data Type into another
#-------------------------------------------------------------------------------
# lets say we have an int x, a bool y, adn a string z
x = 1
y = 2.3
z = "3"

print(x)
print(int(y))   # here we just converted a bool into an int
print(y)
#-------------------------------------------------------------------------------
# if you want to print a string multiple times. you just add a * sign
print(z*4)

#-------------------------------------------------------------------------------
# str conversions
print(z)
z = int(z)
print(z)

#-------------------------------------------------------------------------------
# we have a problem in displaying an int with a string

#print(z + " is a string")          # here z is an int and " is a string" is a string.

# you can not use an int and a string in a same print statement. The fix to this issue is using typcasting.
# Conversion of one datatype to another is called as typecasting. ex: int(), float(), str(), hex(), set(), list() etc.
print()
# fix: TyPEcASTING
print(str(z) + " is a string")
#-------------------------------------------------------------------------------

