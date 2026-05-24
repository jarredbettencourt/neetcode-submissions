class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(ROWS)] for _ in range(COLS)]
        print(new_matrix)
        for r in range(ROWS):
            for c in range(COLS):
                new_matrix[c][r] = matrix[r][c]
        return new_matrix