class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_freq = {}
        for n in nums:
            nums_freq[n] = nums_freq.get(n, 0) + 1
        freq_nums = [[] for _ in range(1, 101)]
        for num, freq in nums_freq.items():
            freq_nums[freq].append(num)
            freq_nums[freq].sort(reverse=True)
        res = []
        for i in range(len(freq_nums)):
            if freq_nums[i]:
                for num in freq_nums[i]:
                    for _ in range(i):
                        res.append(num)
        return res
