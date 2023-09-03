
def multiple(a, b, c):
    for i in range(a, b+1): 
        if(i%c==0): 
            return i
    return -1

def main(): 
    a, b, c = map(int, input().split())
    print(multiple(a,b,c))

main()