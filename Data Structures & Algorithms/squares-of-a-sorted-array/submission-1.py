class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # nums.sort()
        # return nums
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        k = len(nums) - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                res[k] = nums[l] * nums[l]
                l += 1
            else:
                res[k] = nums[r] * nums[r]
                r -= 1
            k -= 1
        return res