# Last updated: 3/22/2025, 11:02:28 PM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases: 1 or more of the lists is empty
        if (not list1) and (not list2):
            return None
        elif (not list1):
            return list2
        elif (not list2):
            return list1
        
        #both lists are nonempty

        #initialise all 4 required nodes
        if list1.val <= list2.val:
            listHead = list1
            listTail = list1
            list1 = list1.next
        else:
            listHead = list2
            listTail = list2
            list2 = list2.next

        while (list1) and (list2):
            if list1.val <= list2.val:
                listTail.next = list1
                listTail = list1
                list1 = list1.next
            else:
                listTail.next = list2
                listTail = list2
                list2 = list2.next
        listTail.next = list1 or list2
        return listHead
