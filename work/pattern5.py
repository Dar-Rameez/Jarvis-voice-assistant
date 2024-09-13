n=5
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))

print()

r=5
for i in range(1,r+1):
    if(i==1 or i==5):
        print("*"*n)
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
        print("")
        