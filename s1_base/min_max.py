dct = dict(
    a=3,
    b=4,
    c=5,
)

print(dct)
# min()
d = zip(dct.values(), dct.keys())
# print(list(d))
e = min(d)
print(e)
