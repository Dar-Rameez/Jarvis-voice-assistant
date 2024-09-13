# s='sameer'
# for i in range(1, 11):
#     print(s)

# s="sameer"
# i=1
# while i<=10:
#     print(s)
#     i+=1

i=1
def show(name):
    global i
    if (i<=10):
        print(name)
        i+=1
        show(name)
show("sameer")