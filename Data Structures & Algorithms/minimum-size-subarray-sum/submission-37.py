class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0 if sum(nums) < target else len(nums)
        l = 0
        cur_sum = nums[l]
        for r in range(1, len(nums)):
            while cur_sum >= target:
                res = min(res, r - l)
                cur_sum -= nums[l]
                l += 1
            cur_sum += nums[r]
        return res