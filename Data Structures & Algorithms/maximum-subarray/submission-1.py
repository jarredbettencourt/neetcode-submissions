class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        maxSub = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            maxSub = max(cur_sum, maxSub)
        return cur_sum