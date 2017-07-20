a = 10
b = 8
c = 11
max = a
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c

print(max)
