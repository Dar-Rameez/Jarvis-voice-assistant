b = 89
def fun():
    global b
    b = 3
    print(b)

fun()
print(b)