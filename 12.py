my_list = ['apple', 'banana', 'orange']
with open("filename.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")
