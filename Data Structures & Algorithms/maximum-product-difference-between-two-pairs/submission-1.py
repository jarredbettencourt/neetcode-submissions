class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        def prod_diff(a, b, c, d):
            return (a * b) - (c * d)
        
        # nums.sort()
        # return prod_diff(nums[-1], nums[-2], nums[0], nums[1])
        max_1, max_2 = 0, 0
        min_1, min_2 = 10001, 10001
        for n in nums:
            if n > max_1:
                max_2 = max_1
                max_1 = n
            elif n > max_2:
                max_2 = n
            if n < min_1:
                min_2 = min_1
                min_1 = n
            elif n < min_2:
                min_2 = n
        return prod_diff(max_1, max_2, min_1, min_2)
