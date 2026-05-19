class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n: int):
            count = 0
            while n:
                i = n % 10
                count += (i ** 2)
                n = n // 10
            return count

        visit = set()
        while n not in visit:
            visit.add(n)
            n = sum_of_squares(n)
            if n == 1:
                return True
        return False