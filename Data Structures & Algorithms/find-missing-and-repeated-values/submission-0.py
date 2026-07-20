class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num_freqs = Counter(grid[0])
        n = len(grid)
        res = [0, 0]
        for i in range(1, len(grid)):
            num_freqs += Counter(grid[i])
        for i in range(1, (n * n) + 1):
            if i not in num_freqs:
                res[1] = i
            elif num_freqs[i] == 2:
                res[0] = i
        return res
