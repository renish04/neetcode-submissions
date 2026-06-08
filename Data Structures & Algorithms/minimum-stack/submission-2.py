class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini == []:
            self.mini.append(val)
        else:
            w = self.mini[-1]
            if val <= w:
                self.mini.append(val)

    def pop(self) -> None:
        w = self.stack.pop()
        if self.mini != []:
            r = self.mini.pop()
            if w != r:
                self.mini.append(r)

    def top(self) -> int:
        w = self.stack[-1]
        return w

    def getMin(self) -> int:
        w = self.mini[-1]
        return w
