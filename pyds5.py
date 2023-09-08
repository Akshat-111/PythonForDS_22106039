str = input("Enter the string: ")
l1 = str.split()
l2=[]
for i in l1:
    l2.append(int(i))
for i in range(0, len(l2)):
    for j in range(i+1,len(l2)):
        if l2[i]>l2[j]:
            l2[i],l2[j]=l2[j],l2[i]
print(l2)