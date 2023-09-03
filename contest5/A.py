a, b = map(int, input().split())
soma = 0
minim = a//  b
if(a-b*minim>0): 
    minim+=1

print(minim)