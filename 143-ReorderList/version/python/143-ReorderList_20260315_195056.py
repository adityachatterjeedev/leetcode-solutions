# Last updated: 3/15/2026, 7:50:56 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        if not head.next:
9            return
10        
11        #find length
12        listlen = 0
13        curr = head
14        while curr:
15            listlen += 1
16            curr = curr.next
17        
18        stop = (listlen) // 2
19
20        count = 0
21
22        curr = head
23        prev = None
24
25        while count < stop:
26            prev = curr
27            curr = curr.next
28            count += 1
29        
30        # cut the two lists off
31        prev.next = None
32        
33        #store the head of the second list
34        second_head = curr
35
36        #Reverse the second list
37        prev = None
38
39        while curr:
40            nxt = curr.next
41            curr.next = prev
42            prev = curr
43            curr = nxt
44
45        second_head = prev
46        
47        p1, p2 = head, second_head
48
49        flag = True
50        while p1 and p2:
51            if flag:
52                p1_nxt = p1.next
53                p1.next = p2
54                p1 = p1_nxt
55                if p1_nxt:
56                    p1_nxt = p1_nxt.next
57            else:
58                p2_nxt = p2.next
59                p2.next = p1
60                p2 = p2_nxt
61                if p2_nxt:
62                    p2_nxt = p2_nxt.next
63            flag = not flag