def dfs(matrix, x, y, r, c):
    if x not in range(r) or y not in range(c) or  matrix[x][y] != 1 :
        return
    matrix[x][y] = 999

    dfs(matrix, x, y+1, r, c)
    dfs(matrix, x+1, y, r, c)
    dfs(matrix, x+1, y+1, r, c)
    dfs(matrix, x-1, y, r, c)
    dfs(matrix, x, y-1, r, c)
    dfs(matrix, x-1, y-1, r, c)
    dfs(matrix, x+1, y-1, r, c)
    dfs(matrix, x-1, y+1, r, c)

def bfs (matrix, x, y, visited, rows, cols):
    q = []
    visited.add((x, y))
    q.append((x,y))
    while len(q):
        row, col = q.pop()
        neighbors = [[1,0], [0,1], [-1,0], [0, -1], [1,1], [-1,1], [1,-1], [-1,-1]]
        for nr, nc in neighbors:
            r , c = row + nr, col+nc
            if r in range(rows) and c in range(cols) and (r,c) not in visited and matrix[r][c] == 1:
                q.append((r,c))
                visited.add((r,c))

def find_noof_islands(matrix):
    if len(matrix) == 0:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    no_of_islands = 0
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                bfs(matrix, r, c, visited, rows, cols)
                no_of_islands+=1
    return no_of_islands

def count_noof_islands(matrix):
    rows = len(matrix)
    if rows == 0:
        return
    cols = len(matrix[0])
    no_of_islands = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] ==1:
                dfs(matrix, i, j, rows, cols)
                no_of_islands+= 1
    return no_of_islands






graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

print(count_noof_islands(graph))
# print(find_noof_islands(graph))