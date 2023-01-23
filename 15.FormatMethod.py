# str.format() : mor control when displaying outputs

animal = "cow"
item = "moon"

#print("The " + animal+ " jumped over the " + item)

#print("The {} jumped over the {}".format(animal,item))

# using keyword argument
#print("The {animal} jumped over the {item}. The {item} was tall!".format(animal="cow",item="stone"))

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

            # add padding
print("The {:10} jumped over the {:10} in LOVE.".format(animal,item))
            # left align
print("The {:<10} jumped over the {:<10} in LOVE.".format(animal,item))    
            # right align
print("The {:>10} jumped over the {:>10} in LOVE.".format(animal,item))
            # center align
print("The {:^10} jumped over the {:^10} in LOVE.".format(animal,item))       
            # also be used in keyword args
print("The {animal:>10} jumped over the {item:>10} in LOVE.".format(animal="Dog",item="Stick"))    