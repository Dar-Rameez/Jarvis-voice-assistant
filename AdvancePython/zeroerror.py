a  = int(input("enter the number: "))
b  = int(input("enter second number: "))
if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide any number by zero")
else:
    print(f"the division a/b is {a/b}")