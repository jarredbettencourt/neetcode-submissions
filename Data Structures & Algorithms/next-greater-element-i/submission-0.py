class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        temp_store = []
        index_store = {n: i for i, n in enumerate(nums2)}
        index_to_item = {index: item for index, item in enumerate(items)}
