n = 5 
file = open("filename.txt", "r")
for _ in range(n):
    line = file.readline()
    print(line)
file.close()
