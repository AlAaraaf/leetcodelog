"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isSameStructure(main: TreeNode, target: TreeNode) -> bool:
            if main == None or target == None:
                return False
            if main.val != target.val:
                return False
            LeftSame = target.left == None or isSameStructure(main.left, target.left)
            RightSame = target.right == None or isSameStructure(main.right, target.right)
            return LeftSame and RightSame

        stack = [A]
        while len(stack) > 0:
            node = stack.pop()
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
            if isSameStructure(node, B):
                return True
        return False