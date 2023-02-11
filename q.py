file = open("text.txt","r")
# 2,13,5
# a,b,c
d = {}
for line in file:
    x = line.split(",")
    a = x[0]
    b = x[1]
    c = x[2]
    d = len(c)- 1
    c = c[0:d]
    d[b] = c
    y = d[b]
    d[a] =y

    print(str(d.values()))
    

    