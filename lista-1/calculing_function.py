def calculate(x):
    soma=0
    for i in range(1, x+1): 
        soma +=((-1)**i)*i
    print(soma)

def main():
    a = int(input())
    calculate(a)
    
if __name__ == "__main__":
    main()