class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        cur_prod = 1
        for r in range(len(nums)):
            cur_prod *= nums[r]
            while l <= r and cur_prod >= k:
                cur_prod //= nums[l]
                l += 1
            res += (r - l + 1)
        return res