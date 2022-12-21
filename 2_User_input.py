# here we will learn how to ask user for their input.

# ask user their name
name = input("what is your name?: ")
# what if the user inputs a string here?
    #what is your name?: shroud
    #What is your age?: twentyOne
    #shroud
    #twentyOne
# This is unacceptable as age has to be an int or float. 
# thats why we need to convert this "age" into an int

age = int(input(("What is your age?: ")))

print("Hello " + name)
print(age)
#-----------------------------------------------------------------