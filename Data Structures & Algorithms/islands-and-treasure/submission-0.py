class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r, c))
    
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = 0
        while q:
            q_length = len(q)
            for _ in range(q_length):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid[nr][nc] == -1 or (nr, nc) in visit:
                        continue
                    grid[nr][nc] = dist + 1
                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1