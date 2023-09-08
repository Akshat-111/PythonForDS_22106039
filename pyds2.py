list1 = []
list2 = []
n1 = int(input("enter size of list 1 : "))
for i in range(n1):
    i = input("Enter the elements: ")
    list1.append(i)
print(list1)
n2 = int(input("enter size of list 2 : "))
for i in range(n2):
    i = input("Enter the element: ")
    list2.append(i)
print(list2)
list3 = list1+list2
print(list3)