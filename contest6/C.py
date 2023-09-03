def main(): 
    N, M, H, K = map(int, input().split())
    S = input()
    coordenada = {}
    for i in range(0, M): 
        x, y = map(int, input().split())
        coordenada[(x, y)] = 1
    x, y = (0, 0)
    for item in S: 
        chega = True
        if(item=='R'):
            x += 1
        elif(item=='L'): 
            x -= 1
        elif(item=='U'): 
            y += 1
        elif(item=='D'): 
            y -= 1
        N-=1
        H-=1
        if H<0: 
            chega = False
            break
        elif H>=0 and (x, y) in coordenada and H<K: 
            coordenada.pop((x, y))
            H = K
        if(N==0): 
            break
    if(chega): 
        print("Yes")
    else: 
        print("No")

main()