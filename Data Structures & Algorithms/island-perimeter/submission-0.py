class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
                return 1
            elif (r, c) in visit:
                return 0

            visit.add((r, c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for rows in range(ROWS):
            for cols in range(COLS):
                if grid[rows][cols] == 1:
                    return dfs(rows, cols)
