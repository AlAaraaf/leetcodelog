"""
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。
这个链表的倒数第 3 个节点是值为 4 的节点。

给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针
        fast_node = head
        while k > 0 and fast_node != None:
            fast_node = fast_node.next
            k -= 1
        
        while fast_node != None:
            fast_node = fast_node.next
            head = head.next
        
        return head

def BuildList() -> ListNode:
    head = ListNode(1)
    start = head
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)
    head = head.next
    head.next = ListNode(4)
    head = head.next
    head.next = ListNode(5)

    return start


test = Solution()
head = BuildList()
k = 5
print(test.getKthFromEnd(head, k).val)
