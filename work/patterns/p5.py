n=5
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))

for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))

m=5
i=1
while(i<=m):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))
    i+=1

m=5
i=m
while(i>=0):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
    i-=1