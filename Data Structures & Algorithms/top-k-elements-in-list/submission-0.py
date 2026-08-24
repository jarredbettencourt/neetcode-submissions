class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}
        for num in nums:
            freq_list[num] = 1 + freq_list.get(num, 0)
        return list(freq_list.keys())[-2:]