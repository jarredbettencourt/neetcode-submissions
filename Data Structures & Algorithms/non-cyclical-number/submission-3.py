class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        sum = str(n)
        while sum != 1:
            sum = 0
            for x in str(n):
                sum += (int(x) ** 2)
            if sum in visit:
                return False
            visit.add(sum)
            n = str(sum)
        return True