class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        dist = float('inf')
        l = 0
        for r in range(k, len(arr) + 1):
            temp_arr = arr[l:r]
            temp_dist = 0
            for i in range(0, k):
                temp_dist += abs(temp_arr[i] - x)
            if temp_dist < dist:
                res = temp_arr
                dist = temp_dist
            l += 1
        return res