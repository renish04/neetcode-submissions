class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini == []:
            self.mini.append(val)
        else:
            w = self.mini.pop()
            self.mini.append(w)
            if val <= w:
                self.mini.append(val)

    def pop(self) -> None:
        w = self.stack.pop()
        if self.mini != []:
            r = self.mini.pop()
            if w != r:
                self.mini.append(r)

    def top(self) -> int:
        w = self.stack.pop()
        self.stack.append(w)
        return w

    def getMin(self) -> int:
        w = self.mini.pop()
        self.mini.append(w)
        return w
