class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = set()
        for num in nums:
            if len(hash_set) > k:
                hash_set.remove(num)
            if num in hash_set:
                return True
            hash_set.add(num)
        return False