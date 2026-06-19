class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ind_dict = defaultdict(list)
        res = []
        for i, n in enumerate(nums):
            if n in ind_dict:
                for index in ind_dict[n]:
                    res.append((index, i))
            ind_dict[n].append(i)
        return len(res)