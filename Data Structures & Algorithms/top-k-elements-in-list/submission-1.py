class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # {1: 1, 2: 2, 3: 3}
        freq_list = [[] for _ in range(len(nums) +1)]
        for num, freq in count.items():
            freq_list[freq].append(num)
        freq_list_len = len(freq_list)
        for i in range(freq_list_len - 1, -1, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res