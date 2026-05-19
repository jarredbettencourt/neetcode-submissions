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
        n = sum_of_squares(n)
        while n != 1:
            if n in visit:
                return False
            visit.add(n)
            n = sum_of_squares(n)
        return True