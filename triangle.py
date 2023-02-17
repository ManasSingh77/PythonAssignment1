a=int(input())
b=int(input())
c=int(input())
if(a+b>c and a+c>b and b+c>a):
   if(a!=b and b!=c and c!=a):
       print("Scalene Triangle")
   elif(a==b!=c or b==c!=a or a==c!=b):
        print("Isosceles Triangle")
   if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2):
       print("Right angle Triangle")
else:
    print("Invalid")
