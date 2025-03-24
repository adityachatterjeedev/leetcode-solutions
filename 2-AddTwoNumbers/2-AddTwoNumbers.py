# Last updated: 3/24/2025, 10:56:27 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def getValue(l):
            if l is None:
                return 0
            
            decimal = 1
            count = 0
            while l is not None:
                count += decimal * l.val
                decimal *= 10
                l = l.next

            return count

    
        num = getValue(l1) + getValue(l2)
        head = ListNode()
        curr = head
        while True:
            curr.val = num % 10
            num = num // 10
            if num == 0:
                break
            nextNode = ListNode()
            curr.next = nextNode
            curr = nextNode
        
        return head
