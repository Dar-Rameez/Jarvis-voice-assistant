a=1
b=2
c=3
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=1
b=23
c=9
print(greatest(a,b,c))