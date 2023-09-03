from math import sqrt

N = int(input())
maior = 0
soma = 0
new = []
for i in range(N): 
    number = int(input())
    if(number%2!=0): 
        print("YES")
    else:
        for i in range(3, int(sqrt(number)), 2): 
            if(number%i == 0): 
                print("YES")
                break

        print("NO")