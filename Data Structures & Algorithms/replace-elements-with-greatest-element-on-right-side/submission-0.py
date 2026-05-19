class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_val = -1
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                greatest_val = arr[i]
                arr[i] = -1
                continue
            tmp = arr[i]
            arr[i] = greatest_val
            greatest_val = max(tmp, greatest_val)
        return arr