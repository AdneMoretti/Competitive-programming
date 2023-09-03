worlds = []


def is_palindrom(a): 

    n = len(a)-1
    for i in range(n): 
        if(a[i]!= a[n-i]): 
            return False

    return True

def main(): 
    N = int(input())
    for i in range(N):
        new = input()
        for world in worlds: 
            if(is_palindrom(new + world)): 
                print("Yes")
                return 
            elif(is_palindrom(world+new)): 
                print("Yes")
                return 
        worlds.append(new)
    print("No")

main()