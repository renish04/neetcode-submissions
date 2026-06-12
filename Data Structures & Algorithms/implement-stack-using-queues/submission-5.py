class MyStack:

    def __init__(self):
        self.dq = deque([])

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        for i in range(len(self.dq)-1):
            x = self.dq.popleft()
            self.dq.append(x)
        y = self.dq.popleft()

        return y

    def top(self) -> int:
        for i in range(len(self.dq)-1):
            x = self.dq.popleft()
            self.dq.append(x)
        y = self.dq.popleft()
        self.dq.append(y)

        return y

    def empty(self) -> bool:
        if self.dq == deque([]):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()