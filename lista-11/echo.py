length = int(input())
n = input()
if n[0:length//2] == n[length//2::]:
    print("Yes")
else: 
    print("No")