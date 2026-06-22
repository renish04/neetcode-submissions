class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.keyval = {}
        self.frequency = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keyval:
            return -1
        else:
            node = self.keyval[key]
            oldcount = node.count 
            node.prev.next = node.next
            node.next.prev = node.prev

            oldleft, oldright = self.frequency[oldcount]
            if oldleft.next is oldright and oldcount == self.minfreq:
                self.minfreq += 1

            node.count += 1

            if node.count not in self.frequency:
                left = Node(0,0)
                right = Node(0,0)
                left.next = right
                right.prev = left
                self.frequency[node.count] = [left, right]

            right = self.frequency[node.count][-1]
            node.prev = right.prev
            right.prev.next = node
            node.next = right
            right.prev = node

        return node.value 


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:              # ADDED: capacity-0 cache stores nothing, bail out
            return

        if key not in self.keyval:
            # NEW key: must evict BEFORE inserting, else the newcomer becomes its own victim
            if len(self.keyval) >= self.capacity:   # CHANGED: check/evict moved here, was at bottom after insert
                left, right = self.frequency[self.minfreq]   # ADDED: grab min bucket before inserting
                lru = left.next                              # ADDED: least-recent node in min bucket
                lru.prev.next = lru.next                     # ADDED: splice victim out
                lru.next.prev = lru.prev                     # ADDED
                self.keyval.pop(lru.key)                     # ADDED: remove evicted key from map

            node = Node(key, value)
            self.keyval[key] = node

            self.minfreq = 1

            if node.count not in self.frequency:
                left = Node(0,0)
                right = Node(0,0)
                left.next = right
                right.prev = left
                self.frequency[node.count] = [left, right]

            right = self.frequency[node.count][-1]
            node.prev = right.prev
            right.prev.next = node
            node.next = right
            right.prev = node

        else:
            node = self.keyval[key]
            node.value = value              # ADDED: update the stored value (was missing — latent bug)
            oldcount = node.count 
            node.prev.next = node.next
            node.next.prev = node.prev

            oldleft, oldright = self.frequency[oldcount]
            if oldleft.next is oldright and oldcount == self.minfreq:
                self.minfreq += 1

            node.count += 1

            if node.count not in self.frequency:
                left = Node(0,0)
                right = Node(0,0)
                left.next = right
                right.prev = left
                self.frequency[node.count] = [left, right]

            right = self.frequency[node.count][-1]
            node.prev = right.prev
            right.prev.next = node
            node.next = right
            right.prev = node

        # REMOVED: the old `if len(self.keyval) > self.capacity:` eviction block that ran AFTER insertion                  



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)