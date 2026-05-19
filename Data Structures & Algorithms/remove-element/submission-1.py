class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
            

# 5, 1, 3, 2, 1, 4, 5
# 5, 3, -1, 2, 1, 4, 5
# 5, 3, 2, -1, 1, 4, 5
# 5, 3, 2, 1, -1, 4, 5
# delte 1
# IR: 5, -1, 3, 2, -1
# FR: 5 3, 2, -1, -1