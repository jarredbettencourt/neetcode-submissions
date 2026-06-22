class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        def prod_diff(a, b, c, d):
            return (a * b) - (c * d)
        
        # max_1, max_2 = -1, -1
        # min_1, min_2 = float('inf'), float('inf')
        # for n in nums:
        #     if n > max_1:
        #         max_1 = n
        nums.sort()
        return prod_diff(nums[-1], nums[-2], nums[0], nums[1])