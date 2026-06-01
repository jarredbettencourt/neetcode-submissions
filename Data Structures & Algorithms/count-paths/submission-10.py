class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        row = [1] * n
        row[-1] = 0
        for i in range(m - 2, -1, -1):
            row[-1] = 1
            for j in range(n - 2, -1, -1):
                row[j] = row[j] + row[j+1]
        return row[0]