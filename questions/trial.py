words = {"hello": 1}
if "hello" in words.keys():
    words["hello"] += 1
else:
    words["hello"] = 1
print(words)