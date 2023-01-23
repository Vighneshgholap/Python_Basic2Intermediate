 # all arguments in a dictionary.
 # accept various keywords arguments into a dictionary

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])

hello(first="Silent",middle="Shrouded",last="Steps")


#Muliple inputs:

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])
    print("Hello ", end="")
    for key, value in kwargs.items():
        print(value, end="")

hello(title="MR.",first="Silent",middle="Shrouded",last="Steps")