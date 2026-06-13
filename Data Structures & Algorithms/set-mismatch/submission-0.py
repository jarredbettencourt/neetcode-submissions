class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        for num, count in num_freq.items():
            if count == 2:
                return [num, num + 1]