# Last updated: 3/15/2026, 11:33:52 PM
1class ListNode:
2
3    def __init__(self, val: int, next = None, prev = None):
4        self.val = val
5        self.next = next
6        self.prev = prev
7
8class MyCircularQueue:
9
10    def __init__(self, k: int):
11        self.capacity = k
12        self.num_elements = 0
13        self.head = None
14        self.tail = None
15
16    def enQueue(self, value: int) -> bool:
17        if self.num_elements == self.capacity:
18            return False
19
20        new_node = ListNode(value)
21
22        if self.num_elements == 0:
23            self.head = new_node
24            self.tail = new_node
25        else:
26            new_node.next = self.tail
27            self.tail.prev = new_node
28            self.tail = new_node
29        self.num_elements += 1
30
31        return True
32
33    def deQueue(self) -> bool:
34        if self.num_elements == 0:
35            return False
36
37        curr = self.head
38        if self.num_elements == 1:
39            self.head = None
40            self.tail = None
41        else:
42            self.head = self.head.prev
43            self.head.next = None
44        del(curr)
45        self.num_elements -= 1
46        return True
47
48
49    def Front(self) -> int:
50        return self.head.val if self.head else -1
51
52    def Rear(self) -> int:
53        return self.tail.val if self.tail else -1
54
55    def isEmpty(self) -> bool:
56        return self.num_elements == 0
57
58    def isFull(self) -> bool:
59        return self.num_elements == self.capacity
60        
61
62
63# Your MyCircularQueue object will be instantiated and called as such:
64# obj = MyCircularQueue(k)
65# param_1 = obj.enQueue(value)
66# param_2 = obj.deQueue()
67# param_3 = obj.Front()
68# param_4 = obj.Rear()
69# param_5 = obj.isEmpty()
70# param_6 = obj.isFull()