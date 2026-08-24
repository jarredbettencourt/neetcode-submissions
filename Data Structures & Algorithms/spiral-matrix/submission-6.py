class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        visit = set()
        def dfs(r, c, path, matrix, visit):
            if len(path) == ROWS * COLS:
                res.append(path.copy())
                return
            if (r,c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
            path.append(matrix[r][c])
            visit.add((r,c))
            dfs(r, c + 1, path, matrix, visit)
            dfs(r + 1, c, path, matrix, visit)
            dfs(r, c - 1, path, matrix, visit)
            dfs(r - 1, c, path, matrix, visit)

        dfs(0, 0, [], matrix, visit)
        print(res)
        return res[0]
