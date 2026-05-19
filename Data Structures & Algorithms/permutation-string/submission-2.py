class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            print(s2[l:r+1])
            if sorted(s2[l:r + 1]) == sorted(s1):
                return True
            l += 1
        return False