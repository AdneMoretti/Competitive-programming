N = int(input())
steps = input().split(' ')
value = 0
j = 0
weeks = ""
for i in range(7 * N): 
    if(j==7): 
        j = 0
        weeks += f"{value} "
        value = 0
    value += int(steps[i])
    j+=1
weeks += f"{value}"
print(weeks)

