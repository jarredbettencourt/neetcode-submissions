class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = set()
        while True:
            count = 0
            n = str(n)
            for x in n:
                count += int(x) ** 2
            n = count
            if count == 1:
                return True
            seen_set.add(count)
            if count in seen_set:
                return False
