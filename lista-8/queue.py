x, a, b = map(int, input().split())

if a + b < x:
    d = b + 1
else:
    d = a + b - x  + 1
    d = b + 1 - d

print(d)