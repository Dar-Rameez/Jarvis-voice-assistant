def f1(n):
    if n==1:
        return 1
    s=n+f1(n-1)
    return s
x=f1(4)
print(x)





# n=4
# t=0
# for i in range(1,n+1):
#     t+=i
# print(t)

# m=4
# t=0
# i=1
# while(i<=4):
#     t=t+i
#     i+=1
# print(t)
