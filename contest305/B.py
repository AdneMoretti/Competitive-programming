N = input()
tamanho = len(N)
if tamanho<=3: 
    print(N)
elif(tamanho==4): 
    print(N[:-1]+"0")
elif(tamanho==5): 
    print(N[:-2]+"00")
elif(tamanho==6): 
    print(N[:-3]+"000")
elif(tamanho==7): 
    print(N[:-4]+"0000")
elif(tamanho==8): 
    print(N[:-5]+"00000")
elif(tamanho==9): 
    print(N[:-6]+"000000")
    