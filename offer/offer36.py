"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
"""

# 二叉搜索树的中序遍历结果 -> 排序链表
# 每次返回：当前node为root的循环双向链表第一个节点
# 当前node的前驱: DoubleList(node.left).right
# 当前node的后继：DoubleList(node.right)
# 原前驱的后继：当前node
# 原后继的前驱：当前node
# 当前第一个节点：DoubleList(node.left)
# 在完成循环双向链表中间部分的构建后才能将头尾相连，不然会进入死循环内

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def treeToDoublyList(self, root: Node) -> Node:        
        if root == None:
            return None
        if root.left != None: # 前驱与root.left连接
            left_res = self.Construct(root.left)
            root.left = left_res[1]
            left_res[1].right = root
        else:
            left_res = [root] # 否则root为开头

        if root.right != None: # 后继与root.right连接
            right_res = self.Construct(root.right)
            root.right = right_res[0]
            right_res[0].left = root
        else:
            right_res = [root] # 否则root为结尾

        # 首尾相连
        left_res[0].left = right_res[-1]
        right_res[-1].right = left_res[0]
        return left_res[0]
    
    def Construct(self, root: Node):
            """
            构建首尾未相连的双向循环链表, 返回头尾
            """
            if root.left == None and root.right == None: # 单元素循环链表
                return root,root
            elif root.left == None: # root为循环链表开头，root.right接入循环部分
                res = self.Construct(root.right)
                root.right = res[0]
                res[0].left = root
                return root,res[1]
            elif root.right == None: # root为循环链表结尾，root.left接入循环部分
                res = self.Construct(root.left)
                root.left = res[1]
                res[1].right = root
                return res[0],root
            else: # root在循环链表中间，left与right都接入循环部分
                left_res = self.Construct(root.left)
                right_res = self.Construct(root.right)
                root.left = left_res[1]
                left_res[1].right = root
                root.right = right_res[0]
                right_res[0].left = root
                return left_res[0],right_res[1]

def CreatTree():
    head = Node(4)
    root = head
    head.left = Node(2)
    head.right = Node(5)
    head = head.left
    head.left = Node(1)
    head.right = Node(3)
    return root

test = Solution()
head = CreatTree()
res = test.treeToDoublyList(head)
root = res.val
while res.right.val != root:
    print(res.val, end = ",")
    res = res.right
print(res.val)
