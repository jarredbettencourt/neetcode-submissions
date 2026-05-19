class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        repeatSet = set()
        maxLength = 0
        for r in range(len(s)):
            while s[r] in repeatSet:
                repeatSet.remove(s[l])
                l += 1
            repeatSet.add(s[r])
            maxLength = max(maxLength, len(repeatSet))
        return maxLength
