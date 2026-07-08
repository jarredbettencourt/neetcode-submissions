class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        char_dict = defaultdict(list)
        for i in range(len(s)):
            char_dict[s[i]].append(i)
        for value in char_dict.values():
            # for i in range(1, len(value)):
            res = max(res, value[-1] - value[0] - 1)
        return res