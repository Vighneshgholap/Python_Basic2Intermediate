# Dictionaries are a (immutable) changable, unordered collection of unique key: value
# Fast coz of Hashing
# Allow us to access a value quickly

capitals = {'USA':'Washington DC', 
            'INDIA' : 'Delhi'}

#print(capitals['INDIA'])               # use square brackets when u know the key and it exists in the dictionary
#print(capitals.get('Germany'))         # this will print is the input value exists
#print(capitals.keys())                 # print all the keys
#print(capitals.values())               # print all the values
#print(capitals.items())                # print all items

capitals.update({'Germany':'Berlin'})   # immutability: adding new key it to the dictionary
capitals.update({'USA':'Las Vegas'})    # change any values of keys

#capitals.pop('USA')                    # Remove specific keys and values     
#capitals.clear()                       # delete all


for key,value in capitals.items():
    print(key + ": " + value)