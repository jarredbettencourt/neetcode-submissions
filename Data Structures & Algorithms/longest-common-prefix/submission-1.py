class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        res = ""
        cont = ""
        i = 0
        s_len = len(strs[0])
        while i < s_len:
            cont += strs[0][i]
            for s in strs:
                if cont not in s:
                    return res
            res = cont
            i += 1
        return res