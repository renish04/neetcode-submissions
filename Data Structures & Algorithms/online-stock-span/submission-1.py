class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = []

    def next(self, price: int) -> int:
        if not self.stack and not self.index:
            self.stack.append(price)
            self.index.append(len(self.stack)-1)
            print(1)
            return 1
        else:
            if self.stack and price < self.stack[-1]:
                self.stack.append(price)
                self.index.append(len(self.stack)-1)
                print(1)
                return 1
            else:
                self.stack.append(price)
                i = len(self.stack)-1
                while self.index and self.stack[self.index[-1]] <= price:
                    self.index.pop()
                if self.stack == []:
                    print(i+1)
                    return i+1
                else:    
                    r = self.index[-1]
                    self.index.append(i)
                    print(i-r)
                    return i - r



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)