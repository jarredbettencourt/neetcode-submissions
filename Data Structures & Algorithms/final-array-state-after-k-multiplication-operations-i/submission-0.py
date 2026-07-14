class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        mapping = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(mapping)
        while k != 0:
            popped_num, popped_idx = heapq.heappop(mapping)
            heapq.heappush(mapping, (multiplier * popped_num, popped_idx))
            k -= 1
        res_arr = [0] * len(nums)
        for n, i in mapping:
            res_arr[i] = n
        return res_arr