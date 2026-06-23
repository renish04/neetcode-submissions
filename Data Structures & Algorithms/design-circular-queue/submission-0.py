class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.arr = [None]*(self.k)
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.rear == self.k - 1:
            if self.arr[0] is None:
                self.rear = 0
                self.arr[self.rear] = value
                return True
            else:
                return False
        else:
            if self.arr[self.rear + 1] is None:
                self.rear = self.rear + 1
                self.arr[self.rear] = value
                return True
            else:
                return False

    def deQueue(self) -> bool: 
        if self.arr[self.front] is not None:
            self.arr[self.front] = None
            if self.front == self.k-1:
                self.front = 0
            else:
                self.front = self.front + 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.arr[self.front]

    def Rear(self) -> int:
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        if self.arr[self.front] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.rear == self.k - 1:
            if self.arr[0] is not None:
                return True
            else:
                return False
        else:
            if self.arr[self.rear + 1] is not None:
                return True
            else:
                return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()