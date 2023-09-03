n = int(input())
people = []
menor = 1000000000
indice_menor = 10000
for i in range(n): 
    s, a = input().split()
    a = int(a)
    people.append(s)
    if(a<menor): 
        menor = a
        indice_menor = i

s = people[indice_menor]
print(s) 
count = indice_menor+1
if(count>n-1): 
    count=0
while(count!= indice_menor): 
    s = people[count]
    print(s)
    count+=1
    if(count>n-1): 
        count=0