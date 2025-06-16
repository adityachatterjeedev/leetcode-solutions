# Last updated: 6/16/2025, 3:23:03 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        front = head
        for _ in range(n):
            front = front.next
        
        if front is None:
            head = head.next
        else:
            prev, curr = None, head
            while front:
                prev = curr
                front = front.next
                curr = curr.next

            #remove
            nextnode = curr.next
            curr.next = None
            prev.next = nextnode

        return head