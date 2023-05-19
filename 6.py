content = ""
with open("filename.txt", "r") as file:
    for line in file:
        content += line
print(content)
