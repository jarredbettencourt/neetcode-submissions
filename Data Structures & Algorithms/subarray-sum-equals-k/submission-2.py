class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_map = {0: 1}
        for n in nums:
            cur_sum += n
            res += prefix_map.get(cur_sum - k, 0)
            prefix_map[cur_sum] = 1 + prefix_map.get(cur_sum, 0)
        return res