class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                 # key -> Node
        self.left = Node(0, 0)          # LRU sentinel
        self.right = Node(0, 0)         # MRU sentinel
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):             # unlink a node from the list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):             # insert just before right (MRU end)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])   # pull out of current position
            self.insert(self.cache[key])   # re-insert at MRU end
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])   # remove old node for this key
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)                  # add at MRU end
        if len(self.cache) > self.cap:
            lru = self.left.next           # the real node next to left sentinel
            self.remove(lru)
            del self.cache[lru.key]