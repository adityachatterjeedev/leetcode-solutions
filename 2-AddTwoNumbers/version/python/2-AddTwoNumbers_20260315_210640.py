# Last updated: 3/15/2026, 9:06:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        num1 = 0
9        multiplier = 1
10        while l1:
11            num1 += (l1.val * multiplier)
12            multiplier *= 10
13            l1 = l1.next
14
15        num2 = 0
16        multiplier = 1
17        while l2:
18            num2 += (l2.val * multiplier)
19            multiplier *= 10
20            l2 = l2.next
21
22        res = num1 + num2
23
24        head = ListNode(res % 10)
25        res = res // 10
26        curr = head
27        while res:
28            new_node = ListNode(res % 10)
29            res = res // 10
30            curr.next = new_node
31            curr = new_node
32
33        return head
34