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
        sum = sum_of_squares(n)
        visit.add(sum)
        while sum != 1:
            if sum in visit:
                return False
            visit.add(sum)
            sum = sum_of_squares(n)
        return True