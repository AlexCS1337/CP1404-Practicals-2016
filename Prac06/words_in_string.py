

text = input("Enter a string: ")
words = {}

for word in text.split(" "):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print(words)