# pack all arguments into a tuple
# it is used when u dont know how many arguments will user input.

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

z = add(3,2,1,12,2,43,1)
print(z)