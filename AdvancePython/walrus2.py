# without walrus operator, it is just a simple program which we already have wrote 
# data = input("Enter some text: ")
# while len(data) >0:
#     print(f"You entered: {data}")
#     data = input("Enter some text: ")

#now use a walrus operator to do same program

while (data := input("Enter some text: ")) != "":
    print(f"You Entered: {data}")