n = int(input("enter the number : "))
ans=""
while(n>0):
    ans=str(n%2)+ans
    n//=2
print((ans))