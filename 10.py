word_count = {}
with open("filename.txt", "r") as file:
    words = file.read().split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
print(word_count)
