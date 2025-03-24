# Last updated: 3/24/2025, 10:47:45 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        s = set()
        temp = head
        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)
                temp = temp.next
        return False