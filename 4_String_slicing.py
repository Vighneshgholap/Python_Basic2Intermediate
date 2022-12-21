# Here we will learn about string slicing:
    # String slicing is the process of getting a portion of a string by 
    # using its indices.
    # string[start : stop : step] where start is the index from which you want to start the string

name = "Shroud Steps"
# this is my name and we need only my first name
first_name = name[0:5]          # if we count the name SHROUD from 0, we should end at 5 but it only prints 4 letters.
                                # start is inclusive but stop is exclusive. That means stop is not included. So u have to do + 1 in stop
first_name = name[0:6]

last_name = name[7:12]      
print(first_name)
print(last_name)


# for string[start: stop : step] -> step: its a jump 

funny_name = name[0::2]         # [0:] this means there is no end, meaning everything after 0
print(funny_name)               # Sru tp -> is what it prints
# this jumps to 2nd index from its position. S then it jumps over h to r
#                                         from r it jumps over o to u 
#                                         and so on...

# we can also reverse a string

reverse = name[::-1]
print(reverse)                   # spetS duorhS: prints
