novo = 0
def convert_base(a, k, new, i): 
    # if(a==0): 
    #     return new
    # number = a%10
    # new += (k ** i) * number
    # i+=1
    # print(new)
    # convert_base(a//10, k, new, i)
    while(a!=0):
        number = a%10
        new += (k ** i) * number
        i+=1
        a=a//10
    return new


def main(): 
    k = int(input())
    a, b= input().split()
    a = int(a)
    b = int(b)
    auxa = 0
    auxb = 0
    i = 0
    j = 0
    print(convert_base(a, k, auxa, i)* convert_base(b, k, auxb, j))

main()