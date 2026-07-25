class Solution:
    def isUgly(self, n: int) -> bool:
        # factors = set()
        # continue = True
        while n != 1:
            for i in [2, 3, 5]:
                if (n % i) == 0:
                    n //= i
                    break
                elif i == 5 and (n % i) != 0:
                    return False
        return True