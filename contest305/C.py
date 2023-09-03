def verify_infection(people, N, D, x1, y1):
    infected = [(x1, y1)]
    people_infected = [False]* N 
    people_infected[0] = True
    for infect in infected:
        x1, y1 = infect
        for i in range(1, N):
            if people[i] in infected:
                continue
            else:
                x, y = people[i]
                distance = ((x - x1) ** 2) + ((y - y1) ** 2)
                if distance <= D ** 2: 
                    infected.append((x, y))
                    people_infected[i] = True
                else: 
                    people_infected[i] = False
    return infected

def main():
    N, D = map(int, input().split())
    x1, y1 = map(int, input().split())
    people = [(x1, y1)]
    for i in range(1, N): 
        x, y = map(int, input().split())
        people.append((x, y))
    people_infected = verify_infection(people, N, D, x1, y1)
    for i in range(0, N): 
        if(people[i] in people_infected): 
            print("Yes")
        else: 
            print("No")

main()