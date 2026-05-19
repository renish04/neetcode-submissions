class MyHashMap:

    def __init__(self):
        self.con = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.key = key
        self.value = value

        self.con[self.key] = self.value

    def get(self, key: int) -> int:
        self.key = key

        if self.con[self.key] == -1:
            return -1
        else:
            return self.con[self.key]

    def remove(self, key: int) -> None:
        self.key = key

        self.con[self.key] = - 1



