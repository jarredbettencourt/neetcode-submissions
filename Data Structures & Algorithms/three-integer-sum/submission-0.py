class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums) - 2):
            while nums[i-1] == nums[i]:
                i += 1
            l, r = i + 1, len(nums) - 1
            while l < r:
                print(nums[i], nums[l], nums[r])
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1    
        return res