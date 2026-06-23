class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # heights_sorted = sorted(heights)
        # res = 0
        # for a, b in zip(heights, heights_sorted):
        #     if a != b:
        #         res += 1
        # return res
        height_list = [0] * 101
        expected = []
        for height in heights:
            height_list[height] += 1
        for i in range(1, 101):
            for _ in range(height_list[i]):
                expected.append(i)
        res = 0
        for a, b in zip(heights, expected):
            res += 1 if a != b else 0
        return res