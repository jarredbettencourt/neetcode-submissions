class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_list = []

        # def set_row_to_zero(r, c):
        #     for i in range(ROWS):

        # def set_col_to_zero(r, c):

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_list.append((i, j))

        for r, c in zero_list:
            for i in range(ROWS):
                for j in range(COLS):
                    if i == r or j == c:
                        matrix[i][j] = 0
        



        