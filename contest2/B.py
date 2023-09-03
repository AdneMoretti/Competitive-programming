
def vertical(H, W, A):
    numbers = []
    for i in range(W): 
        numbers.append(A[0][i])
    for i in range(H): 
        for j in range(W): 
            if(i<H-1): 
                A[i][j] = A[i+1][j]
            else:
                A[i][j] = numbers[j]

def horizontal(A, H, W): 
    numbers = []
    for i in range(H): 
        numbers.append(A[i][0])
    for i in range(H): 
        for j in range(W): 
            if(j<W-1): 
                A[i][j] = A[i][j+1]
            else:
                A[i][j] = numbers[i]

def verifica_matriz(A, B): 
    k = 0 
    if(A==B): 
        return True
    else:
        while(k<H): 
            vertical(H, W, A)
            k+=1
            l = 0
            if(A==B): 
                return True
            while(l<W): 
                horizontal(A, H, W)
                if(A==B): 
                    return True
                l+=1
        l = 0
        while(l<W): 
            horizontal(A, H, W)
            l+=1
            k = 0
            if(A==B): 
                return True
            while(k<H): 
                vertical(H, W, A)
                if(A==B): 
                    return True
                k+=1

H, W = input().split(" ")
H = int(H)
W = int(W)
A = []
B = []
for i in range(H): 
    numbers = input()
    linha = []
    for j in numbers: 
        linha.append(j)
    A.append(linha)

for i in range(H): 
    numbers = input()
    linha = []
    for j in numbers: 
        linha.append(j)
    B.append(linha)

if(verifica_matriz(A, B)):
    print("Yes")
else: 
    print("No")
