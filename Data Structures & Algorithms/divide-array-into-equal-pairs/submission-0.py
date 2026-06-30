class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        array_freq = Counter(nums)
        for freq in array_freq.values():
            if freq % 2 != 0:
                return False
        return True