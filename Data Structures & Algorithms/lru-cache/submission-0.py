class Node:
    def __init__(self, prev = None, value = 0, next = None):
        self.prev = prev
        self.value = value
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key not in self.hashmap or self.hashmap[key].value is None:
            return -1
        else:
            get = self.hashmap[key]
            if get == self.mr:
                return self.hashmap[key].value
            
            elif get == self.lr:
                get.prev.next = get.next
                self.lr = get.prev
                get.prev = None 
                get.next = self.mr
                self.mr.prev = get
                self.mr = get
                return get.value

            else:
                get.prev.next = get.next
                get.next.prev = get.prev
                get.prev = None
                get.next = self.mr
                self.mr.prev = get 
                self.mr = get
                return get.value

    def put(self, key: int, value: int) -> None:
        if not self.hashmap:
            temp = Node(None, value, None)
            self.hashmap[key] = temp
            self.lr = temp
            self.mr = temp
            self.n += 1

        else:
            if self.n < self.capacity:
                if key in self.hashmap and self.hashmap[key].value is not None:
                    rem = self.hashmap[key]
                    if rem.prev:
                        rem.prev.next = rem.next
                    else:
                        self.mr = self.mr.next
                    temp = Node(None, value, self.mr)
                    self.mr.prev = temp
                    self.hashmap[key] = temp
                    self.mr = temp
                    self.n += 1
                else:
                    temp = Node(None, value, self.mr)
                    self.mr.prev = temp
                    self.hashmap[key] = temp
                    self.mr = temp
                    self.n += 1
            else:
                if self.lr.prev:
                    lrnode = self.lr.prev
                    self.lr.prev = None
                    self.lr.value = None
                    self.lr = lrnode
                    lrnode.next = None

                    temp = Node(None, value, self.mr)
                    self.mr.prev = temp
                    self.hashmap[key] = temp
                    self.mr = temp

                else:
                    self.lr.value = None
                    self.lr.next = None

                    temp = Node(None, value, self.mr)
                    self.mr.prev = temp
                    self.hashmap[key] = temp
                    self.mr = temp
                    self.lr = temp

                    
                 

