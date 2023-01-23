# exception is an event dected during execution that interrupt the flow of a program

#user input


#num = int(input("Enter a number to divide: "))
#den = int(input("Enter a number to divide by: "))

#result = num / den
#print(result)

# Using exceptions
try:
    num = int(input("Enter a number to divide: "))
    den = int(input("Enter a number to divide by: "))
    result = num / den

# if you know that there might be any exceptions, always use specific exception tool. ex: 20/0 
except Exception as e:
    print(e)
    print("Something went wrong!")
# print result
else:
    print(result)
# close any files: Always execute!
finally:
    print("This will always execute.")