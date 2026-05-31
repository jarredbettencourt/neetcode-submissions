class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            dp[i] = min(dp[i], 1 + min(dp[i + 1: i + jumps + 1]))
        return dp[0]