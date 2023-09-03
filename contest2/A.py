N, A, B = input().split(" ")
A = int(A)
B = int(B)
N = int(N)

numbers = input().split(" ")
for item, i in enumerate(numbers): 
    numbers[item] = int(i)
print(numbers.index(A+B)+1)

