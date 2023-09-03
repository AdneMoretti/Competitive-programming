import math

def calculate_mdc(a, b):
    mdc = math.gcd(a, b)
    return mdc

x = int(input())
for k in range(0, x):
    input_numbers = input().split()
    nova = []
    for i in input_numbers: 
        nova.append(int(i))
    maior = 0
    for i in range(0, len(nova)):
        for j in range(i+1, len(nova)): 
            result = calculate_mdc(nova[i], nova[j])
            if result > maior: 
                maior = result
    print(maior)