def main():
    try:
        a = int(input("Hey, Enter a number:"))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("i'm in final")
main()