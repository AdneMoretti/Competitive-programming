abriu = 0
s =  ''
new = ""
def verify(a): 
    global abriu, s, new
    b = a
    new = a
    item = a.find('(')
    for i in a: 
        if(a[i]=='(' and abriu==1): 
            abriu = 1
            s = ''
        if(a[i]==')' and abriu==1): 
            abriu = 2
            s += ')'
            a = a.replace(s, '')
            new = a
        if(abriu == 1): 
            s += i  
    if(a!=b): 
        verify(a)

    if(a==b): 
        return a 

def main(): 
    global s, new
    n = int(input())
    a = input()
    verify(a)
    print(new)
main()