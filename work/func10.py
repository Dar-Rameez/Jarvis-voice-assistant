def f2(n):
    if(n==1):
        return 1
    return n*n + f2(n-1)
x=f2(4)
print(x)