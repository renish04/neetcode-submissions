class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2 == []:
            for i in range(len(self.stack1)):
                r = self.stack1.pop()
                self.stack2.append(r)
            w = self.stack2.pop()
            return w
        else:
            w = self.stack2.pop()
            return w

    def peek(self) -> int:
        if self.stack2 == []:
            for i in range(len(self.stack1)):
                r = self.stack1.pop()
                self.stack2.append(r)
            w = self.stack2.pop()
            self.stack2.append(w)
            return w
        else:
            w = self.stack2.pop()
            self.stack2.append(w)
            return w

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()