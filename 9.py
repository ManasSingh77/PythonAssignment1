line_count = 0
with open("filename.txt", "r") as file:
    for line in file:
        line_count += 1
print(line_count)
