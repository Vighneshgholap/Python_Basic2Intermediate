# Random Module

import random

# Using basic random module

# random between 1 to 6
x = random.randint(1,6)
y = random.random()
print(y)
print(x)

# Using .choice
mylist = ["hi", "bye", "how are you?"]
z = random.choice(mylist)
print(z)

# Using .shuffle
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)