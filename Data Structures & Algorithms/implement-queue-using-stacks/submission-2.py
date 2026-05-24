class MyQueue:

    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        if not self.stack_one:
            self.stack_one.append(x)
        else:
            self.stack_two.append(x)

    def pop(self) -> int:
        val = self.stack_one.pop()
        if not self.stack_one:
            while self.stack_two:
                self.stack_one.append(self.stack_two.pop())
        return val

    def peek(self) -> int:
       return self.stack_one[-1] 

    def empty(self) -> bool:
        return not self.stack_one and not self.stack_two


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()