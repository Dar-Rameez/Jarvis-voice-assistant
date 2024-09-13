#Reduce applies a rolling computions to sequential pair of elements
from functools import reduce

l = [1, 2, 3, 4, 5]
def sum(a, b):
    return a+b
print(reduce(sum, l))
# multiple=lambda x,y: x*y #we can use lambda also to multiply or add or anything
# print(reduce(multiple, l))