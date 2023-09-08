str = input("enter the string : ")
lower=0
upper=0
digits=0
symbols=0
for i in str:
    if('a'<i<'z'):
        lower+=1
    elif('A'<i<'Z'):
        upper+=1
    elif('0'<i<'9'):
        digits+=1
    else:
        symbols+=1
alphabets = upper + lower
print(f"no. of alphabets are {alphabets}")
print(f"no. of digits are {digits}")
print(f"no. of symbols are {symbols}")
print(f"no. of upper case alphabets are {upper}")
print(f"no. of lower case alphabets are {lower}")