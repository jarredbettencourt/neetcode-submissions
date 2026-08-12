class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        temp_store = []
        index_store = {n: i for i, n in enumerate(nums2)}
        for n in nums1:
            if n in index_store:
                temp_store.append(nums2[index_store[n]:])
        print(temp_store)
        for i, arr in enumerate(temp_store):
            first = arr[0]
            for n in arr:
                if n > first:
                    res[i] = n
                    break
        return res