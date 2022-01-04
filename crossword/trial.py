dict = {"a": 3, "b": 1, "c": 2, "d": 5, "e": 0}
x = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
print(x)
y = x.keys()
print(y)
z = list(y)
print(z)