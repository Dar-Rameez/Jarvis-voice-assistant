def prime(n,i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    return prime(n,i-1)
n=int(input("Enter the number: "))
s=prime(n,n-1)
if s==1:
    print(f"{n} is a prime")
else:
    print(f"{n} is not prime")