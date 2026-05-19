class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] != val and nums[i] != -1:
                k += 1
            else:
                nums[i] = -1
                nums[i+1], nums[i] = nums[i], nums[i]+1 
        return k        
            

# 5, 1, 3, 2, 1
# delte 1
# IR: 5, -1, 3, 2, -1
# FR: 5 3, 2, -1, -1