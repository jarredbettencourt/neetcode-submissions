class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visit = set()

        def dfs(r, c, orig_color, new_color, visit):
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or image[r][c] != orig_color or (r,c) in visit:
                return
            
            image[r][c] = color 
            visit.add((r,c))
            dfs(r + 1, c, orig_color, color, visit)
            dfs(r, c + 1, orig_color, color, visit)
            dfs(r - 1, c, orig_color, color, visit)
            dfs(r, c - 1, orig_color, color, visit)
            
        dfs(sr, sc, image[sr][sc], color, set())
        return image