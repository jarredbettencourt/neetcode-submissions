class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_freq = Counter(nums)
        res = 0
        for num in nums_freq:
            if nums_freq[num] == 1:
                return -1
            res += math.ceil(nums_freq[num] / 3)
        return res