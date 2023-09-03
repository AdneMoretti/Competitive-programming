N = int(input())
maior = 0
soma = 0
new = []
new = list(map(int, input().split(' ')))
for item in new: 
    if(item > maior): 
        maior = item
for item in new: 
    soma+=maior-item

print(soma)