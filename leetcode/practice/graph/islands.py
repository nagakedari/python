import collections
from typing import List


def no_of_islands(m: List[List[str]]):
    if not m:
        return 0
    rows, cols = len(m), len(m[0])
    visited = set()
    islands_count = 0

    def bfs(r, c):
        q = collections.deque()
        q.append((r, c))
        visited.add((r, c))

        while q:
            r, c = q.popleft()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if row in range(rows) and col in range(cols) and m[row][col] == "1" and (row, col) not in visited:
                    q.append((row, col))
                    visited.add((row, col))


    for r in range(rows):
        for c in range(cols):
            if m[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands_count += 1
    return islands_count


def _no_of_islands_dfs(m):
    rows, cols = len(m), len(m[0])
    islands_count = 0

    def dfs(m, r, c):
        if r not in range(rows) or c not in range(cols) or m[r][c] != "1":
            return
        m[r][c] = "99999"
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            dfs(m, r+dr, c+dc)

    for r in range(rows):
        for c in range(cols):
            if m[r][c] == "1":
                dfs(m, r, c)
                islands_count += 1
    return islands_count


if __name__ == "__main__":
    m = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print(no_of_islands(m))
    print(_no_of_islands_dfs(m))

    m = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    print(no_of_islands(m))
    print(_no_of_islands_dfs(m))