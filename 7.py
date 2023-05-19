import array

lines = array.array('str')
with open("filename.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
print(lines)
