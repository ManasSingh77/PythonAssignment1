a=input("Enter here:")
b=0
for i in range(65,91,1):
    if(a==str(chr(i))):
        b=b+1
for i in range(97,123,1):
    if(a==str(chr(i))):
        b=b+1 
if(b==0):
    print("It is not an alphabet")
else:
    print("It is an alphabet")