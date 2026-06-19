class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        for i in range(len(num) - 3):
            if len(Counter(num[i:i+3])) == 1:
                res.append(int(num[i:i+3]))
        if not res:
            return ""
        max_res = max(res)
        if max_res == 0:
            return "000"
        else:
            return str(max(res))