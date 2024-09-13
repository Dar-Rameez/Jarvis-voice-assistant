n=int(input("inter the row "))
for i in range(1,n+1):
    print("#"*(n-i), end="")
    print("*"*(i), end="")
    print("&")