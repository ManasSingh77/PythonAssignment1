with open("filename.txt", "r") as file:
    words = file.read().split()
    longest_words = sorted(words, key=len, reverse=True)[:5]
    print(longest_words)
