class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = 0
        num_set = set(nums)
        for n in nums:
            count = 1
            m = n - 1
            while m in num_set:
                count += 1
                m -=1
            res = max(res, count)    
        return res