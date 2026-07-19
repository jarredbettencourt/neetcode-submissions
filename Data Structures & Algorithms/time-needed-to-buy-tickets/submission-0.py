class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # highest value is sum of values
        # least value is k * len(tickets)
        return tickets[k] * len(tickets)