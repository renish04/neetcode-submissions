class MyHashSet:

    def __init__(self) :
        self.con = []

    def add(self, key: int) -> None:
        self.key = key
        if self.key not in self.con:
           self.con.append(self.key)

    def remove(self, key: int) -> None:
        self.key = key
        if self.key in self.con:
            self.con.remove(self.key)

    def contains(self, key: int) -> bool:
        self.key = key
        if self.key in self.con:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)