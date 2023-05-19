text_to_append = "This is the appended text."
file = open("filename.txt", "a")
file.write(text_to_append)
file.close()

file = open("filename.txt", "r")
content = file.read()
print(content)
file.close()
