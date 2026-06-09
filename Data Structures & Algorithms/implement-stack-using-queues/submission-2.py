class MyStack:

    def __init__(self):
        self.dq1 = deque()
        self.dq2 = deque()

    def push(self, x: int) -> None:
        self.dq1.append(x)

    def pop(self) -> int:
        if len(self.dq1) == 1:
            r = self.dq1.popleft()
            return r
        else:
            for i in range(len(self.dq1)-1):
                r = self.dq1.popleft()
                self.dq2.append(r)
            w = self.dq1.popleft()
            self.dq1 = self.dq2
            self.dq2 = deque()
            return w

    def top(self) -> int:
        if len(self.dq1) == 1:
            r = self.dq1.popleft()
            self.dq1.append(r)
            return r
        else:
            for i in range(len(self.dq1)-1):
                r = self.dq1.popleft()
                self.dq2.append(r)
            w = self.dq1.popleft()
            self.dq1 = self.dq2
            self.dq1.append(w)
            self.dq2 = deque()
            return w       

    def empty(self) -> bool:
        if self.dq1:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()