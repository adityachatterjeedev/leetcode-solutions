# Last updated: 3/22/2025, 11:02:07 PM
parens = {')' : '(', ']' : '[', '}' : '{'}

class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def push(self, value):
        newNode = LinkedListNode(value)
        if not self.head: # linked list is empty
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def pop(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            val = self.head.value
            self.head = self.head.next
            return val


class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = LinkedListStack()
        for item in list(s):
            if item in ['(', '{', '[']:
                parenStack.push(item)
            else:
                if parenStack.isEmpty():
                    return False
                openParen = parenStack.pop()
                if openParen != parens[item]:
                    return False
        if not parenStack.isEmpty():
            return False
        return True