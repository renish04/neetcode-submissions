class MyHashMap:

    def __init__(self):
        self.con = [[-1, -1] for _ in range(1000000)]

    def put(self, key: int, value: int) -> None:
        self.con[key] = [key, value]

    def get(self, key: int) -> int:
        if self.con[key][0] == -1:
            return -1
        return self.con[key][1]

    def remove(self, key: int) -> None:
        self.con[key] = [-1, -1]