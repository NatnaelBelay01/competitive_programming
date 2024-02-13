class Node:
    def __init__(self, val = -10 , prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = Node()
        self.tail = Node(-10, self.head, None)
        self.head.next = self.tail
        self.store = {}
        self.all = {}

        

    def get(self, key: int) -> int:
        if(key in self.store):

            node = self.all[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            return self.store[key]

        else:
            return -1


    def put(self, key: int, value: int) -> None:
        
        if(key in self.store):
            self.store[key] = value
            node = self.all[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        else:
            if(self.count < self.capacity):
                self.store[key] = value
                node = Node(key, self.head , self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.all[key] = node
                self.count += 1
            else:
                node = self.tail.prev
                self.store.pop(node.val)
                self.all.pop(node.val)
                node.prev.next = self.tail
                self.tail.prev = node.prev
                node.prev = None
                node.next = None
                self.store[key] = value
                node = Node(key, self.head , self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.all[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)