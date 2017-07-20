#coding=utf-8

words_set = set()
with open("myDict2", "r") as f:
    for line in f.readlines():
        word = line.strip().decode("utf-8")
        if len(word) > 0 and word not in words_set:
            words_set.add(word)

print words_set
for word in words_set:
    print word
