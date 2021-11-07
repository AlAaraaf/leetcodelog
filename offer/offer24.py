"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""

from util import createListNode, printListNodes

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None:
            return head
        
        preNode = None
        currentNode = head
        nextNode = currentNode.next

        while nextNode != None:
            currentNode.next = preNode
            preNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next
        
        currentNode.next = preNode
        return currentNode

test = Solution()
tree = [1,2,3,4,5]
root = createListNode(tree)
printListNodes(test.reverseList(root))