"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
0 <= 链表长度 <= 1000

双指针（就是归并的思路
简化一下算法的逻辑
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l2 == None:
            if l1 == None:
                return l2 if l2 != None else None
            else:
                return l1

        if l1.val <= l2.val:
            head = l1
            node1_head = l1
            node1_end = l1
            node2 = l2
        else:
            head = l2
            node1_head = l2
            node1_end = l2
            node2 = l1
            
        # set node1 as the main branch, move node2 into node1
        while node1_end != None and node2 != None:
            # print("{0}, {1}".format(node1_head.val, node2.val))
            if node1_head.val <= node2.val and node1_head.next != None and node1_head.next.val > node2.val:
                node1_end = node1_head.next
                node1_head.next = node2
                while node1_end != None and node2.next != None and node2.next.val < node1_end.val:
                    node2 = node2.next
                node2.next, node2 = node1_end, node2.next
                node1_head = node1_end
            elif node1_head.val <= node2.val and node1_head.next == None:
                node1_head.next = node2
                return head
            elif node1_head.val <= node2.val:
                node1_head = node1_head.next
            else:
                node2 = node2.next
        
        return head

def createListNode(seq):
    if len(seq) == 0:
        return None
    head = ListNode(seq[0])
    node = head
    for i in range(1,len(seq)):
        node.next = ListNode(seq[i])
        node = node.next
    return head

l1 = createListNode([1])
l2 = createListNode([1])
test = Solution()
seq = test.mergeTwoLists(l1,l2)
while seq != None:
    print(seq.val, end=" ")
    seq = seq.next