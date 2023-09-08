lst = []
name = []
dmn = []
n = int(input("enter number of students : "))
for i in range(n):
    str = input("Enter the email IDs: ")
    lst.append(str)
tup = tuple(lst)
for i in tup:
    z = i.split("@")
    name.append(z[0])
    dmn.append(z[1])
tup1 = tuple(name)
tup2 = tuple(dmn)
print(tup)
print(tup1)
print(tup2)