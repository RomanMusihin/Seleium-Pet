word = "sample, list, word"
# print(len(word))
# print(word.count("l"))
# print(word.upper())
# print(word.find("a"))
# print(word.split(", "))

hobby = word.split(', ')
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
result = ", ".join(hobby)
print(result)