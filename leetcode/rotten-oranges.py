def min_time_oranges_to_rot(mat):
    if not mat:
        return -1
    rows, cols = len(mat), len(mat[0])

    minimum_time_required_for_oranges_to_rot =0

    visited = set()

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 2 and (i,j) not in visited:
                dfs(mat, i, j, rows, cols, visited)
                minimum_time_required_for_oranges_to_rot+= 1
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                return -1
    
    return minimum_time_required_for_oranges_to_rot

def dfs (mat, x ,y, r, c, visited):
    if x not in range(r) or y not in range(c) or mat[x][y] == 0 or (x, y) in visited:
        return
    visited.add((x,y))
    mat[x][y] = 2

    dfs(mat, x-1, y, r, c, visited) 
    dfs(mat, x+1, y, r, c, visited)
    dfs(mat, x, y-1, r, c, visited)
    dfs(mat, x, y+1, r, c, visited)

mat = [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]

# mat = [[2, 1, 0, 2, 1],
#          [0, 0, 1, 2, 1],
#          [1, 0, 0, 2, 1]]

print(min_time_oranges_to_rot(mat))