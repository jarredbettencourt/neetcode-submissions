class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        res = 0
        for a, b in zip(heights, heights_sorted):
            if a != b:
                res += 1
        return res