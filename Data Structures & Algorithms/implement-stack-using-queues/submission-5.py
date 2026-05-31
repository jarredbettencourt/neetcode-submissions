class MyStack:

    def __init__(self):
        self.q0 = deque()
        self.q1 = deque()
        self.q_list = [self.q0, self.q1]
        self.cur_q = 0

    def push(self, x: int) -> None:
        self.cur_q  = (self.cur_q + 1)  % 2
        while self.q_list[self.cur_q]:
            self.q_list[(self.cur_q + 1) % 2].append(self.q_list[self.cur_q].popleft())
        self.q_list[self.cur_q].append(x)

    def pop(self) -> int:
        val = self.q_list[self.cur_q].popleft()
        self.cur_q  = (self.cur_q + 1)  % 2
        return val

    def top(self) -> int:
        if self.q_list[self.cur_q]:
            return self.q_list[self.cur_q][0]
        else:
            return self.q_list[(self.cur_q + 1) % 2][0]

    def empty(self) -> bool:
        return not self.q0 and not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()