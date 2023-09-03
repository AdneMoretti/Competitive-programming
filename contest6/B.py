from collections import defaultdict

def verify_matriz(data, N, M): 
    global adjacentes 
    adjacentes = defaultdict(list)
    for i in range(N):
        for j in range(M): 
            if(j==0):
                add_adj(data[i][j], data[i][j+1])
            elif(j==M-1): 
               add_adj(data[i][j], data[i][j-1])
            else: 
                add_adj(data[i][j], data[i][j+1])
                add_adj(data[i][j], data[i][j-1])

def add_adj(initial, neighboor): 
    global adjacentes
    if neighboor not in adjacentes[initial]: 
        adjacentes[initial].append(neighboor)

def main(): 
    global adjacentes
    soma = 0
    m, n = map(int, input().split())
    data = []
    for i in range(n): 
        s = input().split()
        data.append(s)
    verify_matriz(data, n, m)
    for chave in adjacentes: 
        tam = len(adjacentes[chave])
        soma += (m-1)-tam
            

    print(soma//2)

main()

