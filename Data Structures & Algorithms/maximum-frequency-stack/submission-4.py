class FreqStack:

    def __init__(self):
        self.freq_map = {}
        self.group_freq = {1 : []}
        self.max_freq = 1

    def push(self, val: int) -> None:
        if val not in self.freq_map:
            self.freq_map[val] = 1
            self.group_freq[1].append(val)
        
        else:
            self.freq_map[val] += 1
            if self.freq_map[val] > self.max_freq:
                self.max_freq = self.freq_map[val]
                self.group_freq[self.freq_map[val]] = [val]
            else:
                self.group_freq[self.freq_map[val]].append(val)


    def pop(self) -> int:
        w = self.group_freq[self.max_freq].pop()
        self.freq_map[w] -= 1
        if self.group_freq[self.max_freq] == []:
            if self.max_freq != 1:
                self.max_freq -= 1

        return w


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()