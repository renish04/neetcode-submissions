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
        self.left = Node(0, 0)          # LRU sentinel (real nodes start after this)
        self.right = Node(0, 0)         # MRU sentinel (real nodes end before this)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # unlink node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # re-insert just before right sentinel (MRU end)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        # if key exists, unlink the old node first
        if key in self.cache:
            old = self.cache[key]
            old.prev.next = old.next
            old.next.prev = old.prev

        node = Node(key, value)
        self.cache[key] = node

        # insert just before right sentinel (MRU end)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        # evict LRU if over capacity
        if len(self.cache) > self.cap:
            lru = self.left.next            # real node next to left sentinel
            lru.prev.next = lru.next        # unlink it
            lru.next.prev = lru.prev
            self.cache.pop(lru.key)