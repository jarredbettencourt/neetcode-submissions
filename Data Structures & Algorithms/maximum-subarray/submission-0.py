class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        maxSub = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            maxSub = max(cur_sum, maxSub)
        return cur_sum