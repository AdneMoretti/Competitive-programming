k = int(input())
s = input()
if(s.count("T")>s.count("A")): 
    print("T")
elif (s.count("A")>s.count("T")): 
    print("A")
else: 
    if(s.find("T", -2, k+1)<s.find("A", -2, k+1)):
        print("T")
    else: 
        print("A")

