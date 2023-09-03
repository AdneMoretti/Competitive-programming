a = []

def F(a): 
    a[1] = (a[1]+a[0]%10)
    a.pop(0)

    return a

def G(a): 
    a[1] = ((a[1]*a[0])%10)
    a.pop(0)

    return a

def main(): 
    N = int(input())
    novo = input().split()
    a = [int(val) for val in a]

 
        
    

main()