order = input("Do you want to print numbers in\n 1-serial order\n 2-reverse order\n Enter your choice: ")
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
jump = int(input("Enter the jump between the numbers: "))
a=input("1-Horizontal\n2-Vertical\nEnter your choice: ")
if(a=="1"):
    if order == "1" and start > end:
        order = "2" 
    if order == "2" and end > start:
        order = "1"
    if order=="1":
        for i in range(start, end+1, jump):
            print(i,end=" ")
    elif order =="2":
        for i in range(start, end-1, -jump):
                print(i,end=" ")
    else:
        print("Invalid input for order. Please enter either '1' or '2'.")
elif(a=="2"):
    if order == "1" and start > end:
        order = "2" 
    if order == "2" and end > start:
        order = "1"
    if order=="1":
        for i in range(start, end+1, jump):
            print(i)
    elif order =="2":
        for i in range(start, end-1, -jump):
                print(i)
    else:
        print("Invalid input for order. Please enter either '1' or '2'.")
else:
    print("Invalid option. Write 1 or 2")
