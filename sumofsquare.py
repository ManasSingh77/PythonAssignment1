a=int(input("Enter number of natural numbers: "))
sum=0
for i in range(1,a+1,1):
    sum=sum+i**2
print("Sum of square of %d natural number= %d"%(a,sum))