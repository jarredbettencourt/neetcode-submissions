class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # idea here is to shift right pointer until s[l:r] contians a duplicate char
        # when duplicate char is found, record lenght of substring into res with max() and shift left pointer
        # slight optimization is to continue loop if length of current substring is less than res

        res = 0
        l = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, len(char_set))
        return res