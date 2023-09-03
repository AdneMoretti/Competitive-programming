from math import ceil, floor


a, b, x = map(int, input().split())

limit1 = (a + x - 1) // x
limit2 = b // x

print(limit2 - limit1 + 1)
