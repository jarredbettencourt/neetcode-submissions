class Solution:
    def maxDifference(self, s: str) -> int:
        # maximize a1, minimize a2
        max_odd = 0
        min_even = len(s)
        freq_list = collections.Counter(s)
        for letter, freq in freq_list.items():
            if freq % 2 == 0:
                min_even = min(freq, min_even)
            else:
                max_odd = max(freq, max_odd)
        return max_odd - min_even