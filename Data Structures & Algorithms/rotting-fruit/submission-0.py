class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh_fruit = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        
        time = 0
        while q:
            q_length = len(q)
            for _ in range(q_length):
                r, c = q.popleft()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1:
                        fresh_fruit -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        return time if fresh_fruit == 0 else -1