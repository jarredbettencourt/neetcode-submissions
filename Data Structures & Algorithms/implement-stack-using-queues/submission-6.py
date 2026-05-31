class MyStack:

    def __init__(self):
        self.q0 = deque()
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        while self.q0:
            self.q1.append(self.q0.popleft())
        self.q1, self.q0 = self.q0, self.q1

    def pop(self) -> int:
        return self.q0.popleft()

    def top(self) -> int:
        return self.q0[0]

    def empty(self) -> bool:
        return not self.q0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()