class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        else:
            get = self.cache[key]

            get.prev.next = get.next
            get.next.prev = get.prev

            self.right.prev.next = get
            get.prev = self.right.prev
            get.next = self.right
            self.right.prev = get
            
            return get
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev

        node = Node(value, key)
        self.cache[key] = node
        
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        
        if len(self.cache) > self.capacity:
            temp = self.left.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.cache.pop(temp.key)