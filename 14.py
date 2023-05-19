with open("file1.txt", "r") as file1:
    with open("file2.txt", "r") as file2:
        for line1, line2 in zip(file1, file2):
            combined_line = line1.strip() + " " + line2.strip()
            print(combined_line)
