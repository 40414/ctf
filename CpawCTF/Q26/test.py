a = 32134
b = 193127

c = 1584891
d = 3438478

while True:
    if b > a:
        a += c
    elif b < a:
        b += d
    else:
        break
print(a, b)