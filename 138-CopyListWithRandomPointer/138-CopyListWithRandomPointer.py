# Last updated: 6/16/2025, 3:22:48 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        #three passes

        #first pass: create and insert new nodes
        current = head
        while current:
            new_node = Node(current.val, current.next, current.random)
            current.next = new_node
            current = new_node.next

        #second pass: switch random pointers to point to the new nodes
        current = head
        while current:
            current_new = current.next
            current_new.random = current_new.random.next if current_new.random else None
            current = current_new.next
        
        #third pass: split the new list
        new_head = head.next
        curr_old = head
        curr_new = new_head
        
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next
            
        return new_head

        
