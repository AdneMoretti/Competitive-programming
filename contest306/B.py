number = input()
soma = 0
for i in range(64):
    if number[i] == '1':
        soma +=  (2 ** i)
print(soma)
