class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TODO: FUTURE SELF
        # IF YOU COME BACK TO THIS, FIND OUT WHY I NEEDED TO PUT THE IF GUARD HERE
        if m == 1 and n == 1:
            return 1
        row = [1] * n
        row[-1] = 0
        for i in range(m - 2, -1, -1):
            row[-1] = 1
            for j in range(n - 2, -1, -1):
                row[j] = row[j] + row[j+1]
        return row[0]