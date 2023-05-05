def pacific_atlanta_water_flow(m):
    rows, cols = len(m), len(m[0])
    pac, atl = set(), set()

    def dfs(m, r, c, visited, previous_hieght):
        if (r, c) in visited or \
            r not in range(rows) or c not in range(cols) or \
                m[r][c] < previous_hieght:
            return
        visited.add((r,c))
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            row = r+dr
            col = c+dc
            dfs(m, row, col, visited, m[r][c])

    for c in range(cols):
        dfs(m, 0, c, pac, m[0][c])
        dfs(m, rows-1, c, atl, m[rows-1][c])

    for r in range(rows):
        dfs(m, r, 0, pac, m[r][0])
        dfs(m, r, cols-1, atl, m[r][cols-1])
    result = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) in pac and (r, c) in atl:
                result.append([r, c])
    return result

if __name__=="__main__":
    m = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacific_atlanta_water_flow(m))