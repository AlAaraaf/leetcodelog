"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

输入：head = [1,3,2]
输出：[2,3,1]
0 <= 链表长度 <= 10000
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list:
        seq = []
        node = head
        while node != None:
            seq.append(node.val)
            node = node.next
        
        seq_len = len(seq)
        return_seq = []
        for i in range(seq_len):
            return_seq.append(seq[seq_len - 1 - i])

        return return_seq

def createListNode(seq):
    head = ListNode(seq[0])
    node = head
    for i in range(1,len(seq)):
        node.next = ListNode(seq[i])
        node = node.next
    return head

test = Solution()
seq = [1,3,2]
head = createListNode(seq)
print(test.reversePrint(head))