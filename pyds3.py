str = str(input("enter the string : "))
y= str.split()
l1=[]
for i in y:
    b= i.capitalize()
    l1.append(b)
new_str= " ".join(l1)
print(new_str)