class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_map = {}
        for idx, char in enumerate(s):
            if char not in string_map:
                string_map[char] = idx
            else:
                string_map[char] = len(s)
        res = min(string_map.values())
        return -1 if res == len(s) else res