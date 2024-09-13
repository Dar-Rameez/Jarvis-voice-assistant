def rvrs(str):
    if len(str)==1:
        return str
    else:
        return rvrs(str[1:])+str[0]
                #bcd + a  dcba
                #cd  + b  dcb
                #d   + c  _dc
                #d + 
str=input("Enter the string: ")  
s=rvrs(str)
print(s)

#abcd
#dcb