class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0 
        # first diagonal
        n = len(mat)
        for i in range(n):
            res += mat[i][i]
            res += mat[i][n - i - 1]
        return res - (mat[n // 2][n // 2] if n % 2 == 1 else 0)