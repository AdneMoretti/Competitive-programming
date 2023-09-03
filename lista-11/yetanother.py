
def solve(a, b): 
    if(a-b >= 10): 
        div = (a-b)//10
        mod = (a-b)%10
        if mod == 0: 
            return div
        else: 
            return div+1
    else: 
        return 1
def main(): 
    n = int(input())
    for i in range(n): 
        a, b = map(int, input().split())
        if(a>b): 
            print(solve(a, b))
        elif(b>a):
            print(solve(b, a))
        else: 
            print(0)

main()