# Last updated: 6/16/2025, 3:22:47 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #find the middle node
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        #reverse list between slow and end
        before = None
        curr = slow.next
        slow.next = None
        while curr is not None:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        
        #merge the two
        first,second = head, before
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
        