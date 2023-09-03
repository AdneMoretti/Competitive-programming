a = int(input())

result = 0
for i in range(1, int(a**0.5) + 1):
    if i*i <= a:
        result = i*i

print(result)