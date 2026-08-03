r = int(input())
c = int(input())
matrix = [list(map(int, input().split())) for _ in range(r)]
row = max(sum(row) for row in matrix)
col = max(sum(matrix[i][j] for i in range(r)) for j in range(c))
print(max(row+col))