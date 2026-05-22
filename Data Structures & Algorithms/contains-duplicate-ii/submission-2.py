class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l, r = 0, 1
        for l in range(len(nums)):
            while r < len(nums) and (r - l) <= k:
                if  nums[l] == nums[r]:
                    return True
                r += 1
        return False