class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_map = {}
        for idx, char in enumerate(s):
            if char not in string_map:
                string_map[char] = idx
            else:
                del string_map[char]
        print(string_map)
        if string_map:
            return min(string_map.values())
        return -1