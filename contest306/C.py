n = int(input())
number = input().split()
data = {}
s = ''
for i in number:
    if(i in data): 
        data[i] += 1
    else: 
        data[i] = 0


dicionario_ordenado = dict(sorted(data.items(), key=lambda item: item[1]))
print(dicionario_ordenado)
for chave in dicionario_ordenado.keys():
    s += chave + ' '

print(s)