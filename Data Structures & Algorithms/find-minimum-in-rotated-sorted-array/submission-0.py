class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while True:
            m = (l + r) // 2
            # in right half
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m 
            if l == r:
                return nums[l]