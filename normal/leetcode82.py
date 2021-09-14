"""
存在一个按升序排列的链表;
给你这个链表的头节点head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。
返回同样按升序排列的结果链表。
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
输入：head = [1,1,1,2,3]
输出：[2,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 边界维护
        if head == None or head.next == None:
            return head
        
        # 添加头结点，保存前序结点位置，初始化
        HeadNode = ListNode(0,head)
        PreNode = HeadNode
        CurrentNode = PreNode.next

        # 双指针查找重复元素
        while CurrentNode != None and not self.IsEnd(CurrentNode):
            NextNode = CurrentNode.next
            
            # 发现重复元素：删除CurrentNode后的所有同元素结点 -> 删除CurrentNode
            if NextNode != None and  NextNode.val == CurrentNode.val:
                while (NextNode != None and NextNode.val == CurrentNode.val):
                    NextNode = self.DeleteCurrentNode(CurrentNode, NextNode)
                CurrentNode = self.DeleteCurrentNode(PreNode, CurrentNode)
            else:
                PreNode = CurrentNode
                CurrentNode = NextNode

        return HeadNode.next
    
    def IsEnd(self, CurrentNode: ListNode) -> bool:
        return CurrentNode.next == None
    
    def DeleteCurrentNode(self, PreNode: ListNode, CurrentNode: ListNode) -> ListNode:
        PreNode.next = CurrentNode.next
        return PreNode.next
    
def ConvertListIntoListNode(list) -> ListNode:
    if len(list) == 0:
        return None
    idx = 0
    CurrentNode = ListNode(list[0])
    head = CurrentNode
    while idx + 1 < len(list):
        NewNode = ListNode(list[idx + 1])
        CurrentNode.next = NewNode
        CurrentNode = CurrentNode.next
        idx += 1

    return head

test = []
head = ConvertListIntoListNode(test)
solution = Solution()
result = solution.deleteDuplicates(head)
if result != None:
    reslist = [result.val]
    while not solution.IsEnd(result):
        result = result.next
        reslist.append(result.val)
else:
    reslist = []
print(reslist)