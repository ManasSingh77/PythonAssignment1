a=int(input("Enter the number of elements in series:"))
find=int(input("Enter the number to be find:"))
c=0
d=1
for i in range(1,a+1,1):
    e=c+d
    print(c,end=",")
    c=d
    d=e
c=0
d=1
for i in range(1,a+1,1):
    e=c+d
    if(find==c):
        print("Yes the number is in the series")
        break
    c=d
    d=e
else:
    print("The number is not in the series")



    