#Map applies a function to all the items in an input List
l = [2, 3, 4, 5, 6]
square = lambda x: x*x
sqList = map(square, l)
print(list(sqList))