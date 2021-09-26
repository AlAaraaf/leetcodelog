"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

1. 哈希
2. 原地修改
"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList1(self, head: 'Node') -> 'Node':
        if head == None:
            return None
            
        DirMap = {}
        FormalHead = head

        currentNode = head
        while currentNode != None:
            DirMap[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next
        
        currentNode = head
        while currentNode != None:
            newNode = DirMap[currentNode]
            if currentNode.next != None:
                newNode.next = DirMap[currentNode.next]
            if currentNode.random != None:
                newNode.random = DirMap[currentNode.random]
            currentNode = currentNode.next
        
        NewHead = DirMap[FormalHead]
        return NewHead

    def copyRandomList2(self, head: 'Node') -> 'Node':
        
        if head == None:
            return None

        currentNode = head

        # copy list
        while currentNode != None:
            currentNode.next = Node(currentNode.val, currentNode.next)
            currentNode = currentNode.next.next
        
        # copy random nodes
        currentNode = head
        while currentNode != None and currentNode.next != None:
            if currentNode.random != None:
                currentNode.next.random = currentNode.random.next
            currentNode = currentNode.next.next
        
        # split lists
        NewHead = head.next
        currentNode = head
        newNode = NewHead
        while currentNode != None and newNode != None:
            currentNode.next = newNode.next
            currentNode = currentNode.next
            if currentNode != None:
                newNode.next = currentNode.next
            newNode = newNode.next
        
        return NewHead