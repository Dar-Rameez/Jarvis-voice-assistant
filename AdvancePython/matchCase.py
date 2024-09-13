def http_status(status):
    match status: 
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unkown status"
status = int(input("Enter status: "))
print(http_status(status))
