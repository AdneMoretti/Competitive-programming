import sys

a, b, c = map(int, input().split())

soma = sys.maxsize

if (abs(a-b) + abs(b-c)) < soma:
    soma = abs(a-b) + abs(b-c)
if (abs(b-c) + abs(c-a)) < soma:
    soma = abs(b-c) + abs(c-a)
if (abs(c-b) + abs(b-a)) < soma:
    soma = (abs(c-b) + abs(b-a))
if (abs(a-c) + abs(c-b))< soma: 
    soma = abs(a-c) + abs(c-b)
if (abs(b-a) + abs(a-c))< soma:
    soma = abs(b-a) + abs(a-c)
if (abs(c-a) + abs(a-b))< soma: 
    soma = abs(c-a) + abs(a-b)

print(soma)