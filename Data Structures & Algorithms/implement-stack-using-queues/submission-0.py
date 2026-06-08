class MyStack:

    def __init__(self):
        self.dq1 = deque()
        self.dq2 = deque()

    def push(self, x: int) -> None:
        self.dq1.append(x)

    def pop(self) -> int:
 
        if len(self.dq1) == 1:
            w = self.dq1.popleft()
            return w
        else:
            for i in range(len(self.dq1)-1):
                m = self.dq1.popleft()
                self.dq2.append(m)

            w = self.dq1.popleft()
            self.dq1 = self.dq2
            return w

    def top(self) -> int:

        if len(self.dq1) == 1:
            w = self.dq1.popleft()
            self.dq1.append(w)
            return w
        else:
            for i in range(len(self.dq1)-1):
                m = self.dq1.popleft()
                self.dq2.append(m)
            w = self.dq1.popleft()
            self.dq2.append(w)
            self.dq1 = self.dq2
            print(w)
            return w
        

    def empty(self) -> bool:

        if len(self.dq1) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()