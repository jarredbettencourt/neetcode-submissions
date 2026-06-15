class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        def dfs(r, c, start_r, start_c):
            print(r, c, start_r, start_c)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if grid[r][c] == 1 and start_r != r and start_c != c:
                return True

            return dfs(r + 1, c, start_r, start_c) or dfs(r, c + 1, start_r, start_c) or dfs(r - 1, c, start_r, start_c) or dfs(r, c - 1, start_r, start_c)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and dfs(r, c, r, c): res += 1
        return res