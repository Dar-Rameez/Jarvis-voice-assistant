def star(num):
    if num==0:
        return
    else:
        star(num-1)
        print("* "*num)


num=int(input("Enter the Number: "))
star(num)