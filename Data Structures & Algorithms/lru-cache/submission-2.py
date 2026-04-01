class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)     
            self.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]    
        if len(self.cache) >= self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
   
    def remove(self, node):
       node.prev.next = node.next  
       node.next.prev = node.prev


    def insert(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node