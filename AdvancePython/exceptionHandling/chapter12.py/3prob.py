try :
    a = int(input("enter a: "))
    b = int(input("enter b6: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")