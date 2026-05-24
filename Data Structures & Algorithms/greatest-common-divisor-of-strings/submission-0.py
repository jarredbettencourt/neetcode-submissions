class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        min_string = str1 if len(str1) < len(str2) else str2
        r = 0, 0
        for r in range(len(min_string)):
            cont_string = min_string[0:r + 1]
            temp_gcd = ""
            while len(temp_gcd) < len(str1) and len(temp_gcd) < len(str2):
                temp_gcd += cont_string
                if temp_gcd == str1 or temp_gcd == str2:
                    return cont_string
        return ""
