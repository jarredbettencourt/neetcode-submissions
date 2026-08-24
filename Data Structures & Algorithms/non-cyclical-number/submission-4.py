class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n: int):
            count = 0
            while n:
                i = n % 10
                count += i ** 2
                n = n // 10
            return count

        visit = set()
        while True:
            sum = sum_of_squares(n)
            if sum == 1:
                return True
            elif sum in visit:
                return False
            visit.add(sum)
