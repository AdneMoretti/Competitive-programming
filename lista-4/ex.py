X = int(input())
result = 0
for i in range(1, X): 
    number = i*i
    if(number<=X):
        result = number
    else: 
        break
    
print(result)