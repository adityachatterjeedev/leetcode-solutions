# Last updated: 3/24/2025, 10:53:09 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        temp = head
        while temp is not None:
            values.append(temp.val)
            temp = temp.next
        
        i = len(values) - 1
        while head is not None:
            if head.val != values[i]:
                return False
            head = head.next
            i -= 1
        return True