class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return n
            hash_set.add(n)