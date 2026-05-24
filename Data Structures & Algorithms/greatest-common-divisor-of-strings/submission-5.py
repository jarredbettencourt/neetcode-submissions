class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        min_string = str1 if len(str1) < len(str2) else str2
        r = 0
        for r in range(len(min_string)):
            cont_string = min_string[0:r + 1]
            temp_gcd = ""
            gcd_s1, gcd_s2 = False, False
            while len(temp_gcd) < max(len(str1), len(str2)):
                temp_gcd += cont_string
                if temp_gcd == str1:
                    gcd_s1 = True
                if temp_gcd == str2:
                    gcd_s2 = True
                if gcd_s1 and gcd_s2:
                    res = cont_string
        return res
