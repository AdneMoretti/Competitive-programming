def count_triangles(A, B, C, D):
    count = 0

    for x in range(A, B+1):
        for y in range(x, C+1):
            for z in range(y, D+1):
                if x + y > z:
                    count += 1

    return count

# Read input
A, B, C, D = map(int, input().split())

# Count the number of triangles
result = count_triangles(A, B, C, D)

# Print the result
print(result)