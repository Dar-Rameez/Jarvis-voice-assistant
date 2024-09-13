def sum(n):
    if(n==1):
        return 1
    return sum(n)
n=int(input("Enter the number: "))
print(sum(n))