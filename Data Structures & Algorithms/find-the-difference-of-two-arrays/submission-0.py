class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_one = set(nums1)
        set_two = set(nums2)

        return [list(set_one - set(nums2)), list(set_two - set(nums1))]