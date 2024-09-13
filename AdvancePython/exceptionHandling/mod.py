def myFunc():
    print("Hello World!")

if __name__ == "__module__":
    #if this code is directly executed by running the file its present in!
    print("we are directly running this code")
myFunc()
print(__name__)