class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 
        visit = set()
        # Do DFS, and for each island, save max of island area vs max already found
        def dfs(r, c):
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or (r, c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            # res = max(res, island_sum)
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res