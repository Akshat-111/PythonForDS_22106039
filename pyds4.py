l1=[]
n1 = int(input("enter size of list 1 : "))
for i in range(n1):
    i = int(input("Enter the elements: "))
    l1.append(i)
print(l1)
y = input("do you want to insert or delete an element ?")
if y=='insert':
    pos = int(input("enter the position where you want to insert the element : "))
    ele = int(input("enter the element you want to insert"))
    l1.insert(pos,ele)
else:
    z = input("do you want to delete the element by value , index or slice of elements ?")
    if z=='value':
        val= int(input("enter value you want to delete :"))
        l1.remove(val)
    elif z=='index':
        idx= int(input("enter the index at which you want to delete :"))
        l1.pop(idx)
    elif z=='slice':
        n1=int(input("enter the starting index : "))
        n2=int(input("enter the ending index : "))
        l1[n1:n2]=[]
    else:print("invalid choice")
print(l1)