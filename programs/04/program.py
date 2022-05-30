import string

text = open("fruit.txt", "r")
d = {}
for l in text:
    l = l.strip().lower()
    l = l.translate(str.maketrans("", "", string.punctuation))
    words = l.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
print(d)
for key in d:
    print(key, ":", d[key])
