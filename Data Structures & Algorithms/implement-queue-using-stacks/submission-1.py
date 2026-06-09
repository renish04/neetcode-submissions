class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if stack2:
            w = stack2.pop()
            return w
        else:
            for i in range(len(stack1)):
                r = stack1.pop()
                stack2.append(r)
            w = stack2.pop()
            return w

    def peek(self) -> int:
        if stack2:
            w = stack2[-1]
            return w
        else:
            for i in range(len(stack1)):
                r = stack1.pop()
                stack2.append(r)
            w = stack2[-1]
            return w

    def empty(self) -> bool:
        if not stack1 and not stack2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()