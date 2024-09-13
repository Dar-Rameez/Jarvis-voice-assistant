n=int(input("Enter the Number:-- "))
if n>1:
    for i in range(2, n):
        if n%i==0:
            print(f"{n} is not prime")
            break
        else:
            print(f"{n} is a prime")
            break