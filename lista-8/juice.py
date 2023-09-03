N = int(input())
numbers = input().split()
soma = 0
for item in numbers: 
    soma += (int(item)/100)
resultado = "{:.12f}".format(round((soma/N)* 100, 12))
print(resultado)

