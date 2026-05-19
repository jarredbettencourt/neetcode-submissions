class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        res = ""
        cont = ""
        i = 0
        while True:
            cont += strs[0][i]
            for s in strs:
                if cont not in s:
                    return res
            res = cont
            i += 1