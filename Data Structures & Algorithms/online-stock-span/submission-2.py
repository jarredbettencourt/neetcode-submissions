class StockSpanner:

    def __init__(self):
        self.write_stack = []

    def next(self, price: int) -> int:
        self.write_stack.append(price)
        self.cur_stack = self.write_stack[:-1]
        res = 1
        while self.cur_stack and price >= self.cur_stack[-1]:
            self.cur_stack.pop()
            res += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)