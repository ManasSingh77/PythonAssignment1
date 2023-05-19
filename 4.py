n = 5  
with open("filename.txt", "r") as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]
    for line in last_n_lines:
        print(line)
