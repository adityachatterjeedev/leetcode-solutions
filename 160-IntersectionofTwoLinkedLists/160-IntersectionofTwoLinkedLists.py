# Last updated: 3/24/2025, 10:49:18 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(m + n) time, O(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        #traverse both linked lists and store their length
        lengthA = 0
        tempA = headA
        while tempA:
            lengthA += 1
            tempA = tempA.next

        lengthB = 0
        tempB = headB
        while tempB:
            lengthB += 1
            tempB = tempB.next
        
        if lengthA < lengthB:
            tempB = headB
            for _ in range(lengthB - lengthA):
                tempB = tempB.next
            tempA = headA
        elif lengthB < lengthA:
            
            tempA = headA
            for _ in range(lengthA - lengthB):
                tempA = tempA.next
            tempB = headB
        else:
            tempA = headA
            tempB = headB
        
        while tempB and tempA:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
        
        return None

