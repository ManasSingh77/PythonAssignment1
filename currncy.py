a=int(input("Enter Rs "))
a=a-100
b=a//2000
e=a%2000
c=e//500
f=e%500
d=f//100
print("Number of 2000 notes =%d 500 notes=%d and 100 notes=%d"%(b,c,d+1))
