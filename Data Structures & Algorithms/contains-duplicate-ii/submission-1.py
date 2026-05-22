class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l, r = 0, 1
        for l in range(len(nums)):
            if r < len(nums) and nums[l] == nums[r]:
                return True
            if (r - l) == k:
                r += 1
        return False