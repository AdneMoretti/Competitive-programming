n = int(input())
a = input()
new = ""
for i in a: 
    code = ord(i)
    code = (code - 65 + n) % 26 + 65
    new += f"{chr(code)}"

print(new)
