class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_freq = {i: -1 for i in range(1, len(nums) + 1)}
        res = []
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num)
            if num_freq[num] == 1:
                res.append(num)
        for num, freq in num_freq.items():
            if freq == -1:
                res.append(num)
        return res