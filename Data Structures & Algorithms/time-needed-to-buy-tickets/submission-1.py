class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # highest value is sum of values
        # least value is k * len(tickets)
        # return tickets[k] * len(tickets)
        tickets_copy = list(enumerate(tickets))
        dq = deque(tickets_copy)
        res = 0
        while True:
            i, n = dq.popleft()
            res += 1
            if i == k and n == 1:
                return res
            else:
                if (n - 1) == 0:
                    continue
                dq.append((i, n-1))