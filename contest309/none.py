

def solve(s, matrice): 
    for linha in matrice: 
        if(linha.count(s)): 
            print("1Yes")
            return 1
    print("No")
    return 0

def main(): 
    matrice = ['123', '456', '789']
    s = ''

    A, B = input().split()
    s = A + B
    solve(s, matrice)


main()