class Solution:

    def __init__(self, w: List[int]):
        self.sum = sum(w)
        self.prob_list = []
        for idx, weight in enumerate(w):
            for _ in range(int((weight / self.sum) * 10000)):
                self.prob_list.append(idx)

    def pickIndex(self) -> int:
        return random.choice(self.prob_list)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()