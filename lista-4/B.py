p = int(input())

def euler_totient(n):
    phi = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            phi -= phi // i
        i += 1
    if n > 1:
        phi -= phi // n
    return phi

result = euler_totient(p - 1)
print(result)