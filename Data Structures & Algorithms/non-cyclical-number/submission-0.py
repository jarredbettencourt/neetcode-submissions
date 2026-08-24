class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = set()
        count = 0
        while True:
            n = str(n)
            count = 0
            for x in n:
                count += int(x) ** 2
            if count == 1:
                return True
            seen_set.add(count)
            if count in seen_set:
                return False