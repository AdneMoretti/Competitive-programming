def solve(x, y, a, n): 
    min = (x//y)
    soma = min*y
    min = min*n
    i = 0
    while(soma<=x): 
        soma+=a[i]
        i+=1
        if(i>=n): 
            i=0
        min+=1
    print(min)


def main(): 
    N = int(input())
    a = input().split()
    x = int(input())
    y = 0
    novo = [int(val) for val in a]
    for item in  novo:
        y += (item)
    solve(x, y, novo, N)


main()