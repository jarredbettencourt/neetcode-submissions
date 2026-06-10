class StockSpanner:

    def __init__(self):
        self.read_stack = []
        self.write_stack = []

    def next(self, price: int) -> int:
        self.write_stack.append(price)
        self.read_stack = self.write_stack[:]
        res = 0
        self.read_stack.pop()
        while self.read_stack and price > self.read_stack[-1]:
            self.read_stack.pop()
            res += 1
        return res + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)