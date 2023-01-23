# index operator []: gives access to a sequence's element 

name = "Hello World"

if(name[0].isupper()):
    name = name.lower()

print(name)

first_word = name[0:5]
print(first_word.upper())