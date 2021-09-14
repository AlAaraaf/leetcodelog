"""
重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

TODO: 改成非递归写法
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        
        print("current lists:")
        print("preorder: ", preorder)
        print("inorder: ", inorder)
        
        # 边界控制
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        # 找到当前剩余队列中的根结点
        currentNode = TreeNode(preorder[0])

        # 划分左右子树
        for i in range(0, len(inorder)):
            if inorder[i] == preorder[0]:
                break
        
        leftTreeInOrder = inorder[:i] if i > 0 else []
        leftTreePreOrder = preorder[1 : i + 1] if i > 0 else []
        rightTreeInOrder = inorder[i + 1:] if i + 1 < len(inorder) else []
        rightTreePreOrder = preorder[i + 1 :] if i + 1 < len(preorder) else []

        # 建立左子树
        currentNode.left = self.buildTree(leftTreePreOrder, leftTreeInOrder)        

        # 建立右子树
        currentNode.right = self.buildTree(rightTreePreOrder, rightTreeInOrder)

        return currentNode

def PrintTree(root: TreeNode):
    queue = [root]
    tree_val = []
    while len(queue) > 0:
        current_node = queue.pop(0)
        tree_val.append(current_node.val)
        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)
    
    print(tree_val)

test = Solution()
preorder = [3,20,7,11]
inorder = [3,20,7,11]
res = test.buildTree(preorder = preorder, inorder = inorder)
PrintTree(res)