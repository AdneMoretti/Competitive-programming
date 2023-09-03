N = int(input())
S = input()
T = input()
similar = True
for i in range(0, N): 
    if(S[i]!=T[i]): 
        if (S[i]=='0' and T[i]=='o') or (S[i]=='o' and T[i]=='0'): 
            pass
        elif (S[i]=='l' and T[i]=='1') or (S[i]=='1' and T[i]=='l'): 
            pass
        else: 
            similar = False
    if not similar: 
        break
if(similar): 
    print("Yes")
else: 
    print("No")
