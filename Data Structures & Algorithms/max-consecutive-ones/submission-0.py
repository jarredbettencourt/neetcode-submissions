class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        running_count = 0
        for n in nums:
            if n == 0:
                running_count = 0
            if n == 1:
                running_count += 1
                res = max(running_count, res)
        return res