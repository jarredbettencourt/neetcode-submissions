class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for idx, n in enumerate(nums):
            if idx % 2 == 0:
                sum1 += n
            else:
                sum2 += n
        return max(sum1, sum2)