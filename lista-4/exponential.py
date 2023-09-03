from math import sqrt

a = int(input())
if(a == 1): 
    print('1')
else: 
    raiz = int(sqrt(a))
    maior = 0
    for i in range(2, raiz+1): 
        p = 2
        while(i ** p <= a): 
            if((i ** p) > maior) :
                maior = i ** p
            p+=1
        
    print(maior)