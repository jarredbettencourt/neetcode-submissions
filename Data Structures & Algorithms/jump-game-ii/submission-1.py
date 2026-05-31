class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 0
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            dp[i] = 1 + min(nums[i + 1: i + jumps + 1])
        print(dp)
        return dp[0]