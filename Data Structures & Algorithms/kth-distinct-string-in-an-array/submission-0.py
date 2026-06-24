class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_freq = Counter(arr)
        for n in arr:
            if arr_freq[n] == 1:
                k -= 1
                if k == 0:
                    return n
        return ""