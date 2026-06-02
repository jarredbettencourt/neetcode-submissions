class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.prefix_grid = [[0 for _ in range(self.COLS + 1)] for _ in range(self.ROWS + 1)]
        for r in range(1, self.ROWS + 1):
            for c in range(1, self.COLS + 1):
                self.prefix_grid[r][c] = matrix[r-1][c-1] + self.prefix_grid[r-1][c] + self.prefix_grid[r][c-1] - self.prefix_grid[r-1][c-1]
        print(self.prefix_grid)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.prefix_grid[row2][col2] - self.prefix_grid[row2][col1-1] - self.prefix_grid[row1-1][col2] + self.prefix_grid[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)