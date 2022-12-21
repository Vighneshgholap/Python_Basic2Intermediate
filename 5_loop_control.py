# Loop control statements = change a loops execution from its normal sequence
# There are 3 types: 
#       Break:          terminate loop
#       continue:       skips to next iteration 
#       Pass:           Placeholder, it does nothing

# Break will terminate entire iteration or loop
while True:
    i = input("What is your name: ")

    if i != "":
        break

# Continue will skip the next code 
    # lets say we have a phone number 813-555-6666
    # and we need to print the number without the "-"
num = "813-555-6666"
for i in num:
    if i == "-":
        continue
    print(i, end="")
print()

# Pass will do nothing 
    # lets say we have a phone number 813-555-6666
    # and we need to print the number without the "-"
num = "813-111-2222"
for i in num:
    if i == "-":
        pass
    else:
        print(i, end="")