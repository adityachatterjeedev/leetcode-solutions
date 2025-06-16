# Last updated: 6/16/2025, 3:22:46 PM
class LLNode:
    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_entries = 0 # num. entries
        self.head: LLNode = None
        tailnode = LLNode(key = "tailnode")
        self.tail = tailnode
        self.hashmap = {} # hashmap. Format = key -> (value, node) (to speed up get)

    def push_to_head(self, node: LLNode):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def move_to_head(self, node: LLNode):
        if node.prev is not None: #node is already head
            nodeprev = node.prev
            nodenext = node.next
            nodeprev.next = nodenext
            nodenext.prev = nodeprev
            node.prev = None
            self.push_to_head(node)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_head(self.hashmap[key][1])
            return self.hashmap[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key][0] = value
            self.move_to_head(self.hashmap[key][1])
        else:
            newnode = LLNode(key)
            self.hashmap[key] = [value, newnode]
            if self.num_entries == 0:
                newnode.next = self.tail
                self.tail.prev = newnode
                self.head = newnode
                self.num_entries = 1
            else:
                self.push_to_head(newnode)
                if self.num_entries == self.capacity:
                    rem_node = self.tail.prev
                    del self.hashmap[rem_node.key]
                    prevnode = rem_node.prev
                    prevnode.next = self.tail
                    self.tail.prev = prevnode
                    del(rem_node)
                else:
                    self.num_entries += 1