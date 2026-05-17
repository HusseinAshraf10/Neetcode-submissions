class Node:
    def __init__(self, key = 0, val = 0):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    def remove(self, node):
        node.next.prev, node.prev.next = node.prev, node.next

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.map) == self.cap:
                lru = self.tail.prev
                self.remove(lru)
                del self.map[lru.key]
            new_node = Node(key, value)
            self.map[key] = new_node
            self.insert(new_node)

