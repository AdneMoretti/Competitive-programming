def construct_matrix(n):
    if n == 1:
        return [[1]]

    # Inicializar matriz com números sequenciais de 1 a n^2
    matrix = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            matrix[i][j] = num
            num += 1

    # Verificar se a soma das linhas é par e fazer ajustes
    for i in range(n):
        if sum(matrix[i]) % 2 == 0:
            matrix[i][-1], matrix[i][-2] = matrix[i][-2], matrix[i][-1]

    # Verificar se a soma das colunas é par e fazer ajustes
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) % 2 == 0:
            matrix[-1][j], matrix[-2][j] = matrix[-2][j], matrix[-1][j]

    # Verificar se a soma das diagonais é par e fazer ajustes
    if sum(matrix[i][i] for i in range(n)) % 2 == 0:
        matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
    if sum(matrix[i][n - i - 1] for i in range(n)) % 2 == 0:
        matrix[0][n - 1], matrix[1][n - 2] = matrix[1][n - 2], matrix[0][n - 1]

    return matrix


# Ler a entrada do usuário
n = int(input())

# Construir e imprimir a matriz
matrix = construct_matrix(n)
for row in matrix:
    print(' '.join(map(str, row)))
