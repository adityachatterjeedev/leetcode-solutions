# Last updated: 3/16/2026, 1:03:28 AM
class LinkedList:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key
        self.value: int = value
        self.prev: 'LinkedList | None' = None
        self.next: 'LinkedList | None' = None


class LRUCache:
    """
     LRU                     MRU
     head <-> N nodes... <-> tail
    """

    def _remove_node(self, node: LinkedList) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def _add_to_tail(self, node: LinkedList) -> None:
        # A <-> TAIL
        # becomes
        # A <-> NODE
        self.tail.prev.next = node
        node.prev = self.tail.prev

        # A <- TAIL becomes
        # NODE <-> TAIL
        node.next = self.tail
        self.tail.prev = node

    
    def _evict(self) -> None:
        # HEAD <-> LRU <-> NODE becomes
        # HEAD <-> NODE
        lru = self.head.next
        self.head.next = lru.next
        lru.next.prev = self.head

        # Delete from cache
        del self.cache[lru.key]


    def __init__(self, capacity: int) -> None:
        self.cache: dict[int, int] = dict()
        self.capacity: int = capacity
        self.head: LinkedList = LinkedList(0, 0)
        self.tail: LinkedList = LinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove_node(node)
        self._add_to_tail(node)
        return node.value

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict()
            node = LinkedList(key, value)
            self.cache[key] = node
            self._add_to_tail(node)
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)