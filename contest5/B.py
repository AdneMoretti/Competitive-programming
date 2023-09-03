def verify_neighboors(aux, data): 
    c = ['s', 'n', 'u', 'k', 'e']
    directions = [(-1, 0), (1,0), (0,-1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1,-1)]
    for item in aux: 
        for direction in directions: 
            new = [item]
            response = verify_next(item, direction, c, data, 1, new)
            if(response): 
                return new

def verify_next(position, direction, c, data, i, new): 
    x, y = position
    dx, dy = direction
    x+=dx
    y+=dy
    if(confirm(x, y) and i<5):
        if(data[x][y]==c[i]): 
            new.append((x, y))
            verify_next((x,y), direction, c, data, i+1, new)
    if(len(new)==5 and i==1): 
        return 1
    else: 
        return 0

def confirm(x, y): 
    return x >= 0 and x < h and y >= 0 and y < w

def main(): 
    global w, h
    h, w = map(int, input().split())
    data = []
    aux = []
    for i in range(h): 
        s = input()
        for j, c in enumerate(s): 
            if(c=='s'):
                aux.append((i, j))
        data.append(s)
    new = verify_neighboors(aux, data)
    for i in new: 
        x, y = i
        print(x+1, y+1)

main()


