class Pills: 
    def __init__(self, A, B): 
        self.a = A
        self.b = B


def main(): 
    iterator = 0
    new = []
    index = 0
    maior = 0
    N, K = map(int, input().split())
    for i in range(N): 
        A, B = map(int, input().split())
        if(A > maior): 
            maior = A
        new.append(Pills(A, B)) 
    #while iterator < maior: 
    #    soma = 0
    #    iterator+=1
    #    for i, item in enumerate(new): 
    #        if(iterator <= item.a): 
    #            soma += item.b
    #            index = i
    #    if(soma <= K): 
    #        print(index)
    #        break
    #    else:
    #        continue

        

main()