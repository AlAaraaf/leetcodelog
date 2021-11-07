"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

题目保证链表中节点的值互不相同
"""

from util import createListNode, printListNodes

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        
        preNode = None
        currentNode = head

        while currentNode.val != val and currentNode.next != None:
            preNode = currentNode
            currentNode = currentNode.next
        
        # 处理位于头结点的情况
        if currentNode == head:
            return currentNode.next
        
        preNode.next = currentNode.next
        return head

test = Solution()
listnodes = [4,5,1,9]
head = createListNode(listnodes)
val = 9
printListNodes(test.deleteNode(head, val))