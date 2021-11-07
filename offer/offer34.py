from util import createTreeNodeByLayerSeq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list:
        
        self.res = []
        self.CurrentRes = []

        def findTarget(root: TreeNode, currentSum: int) -> None:
            currentSum += root.val
            self.CurrentRes.append(root.val)
            # print("location: {0}, currentSum: {1}, currentRes: {2}".format(root.val, currentSum, self.CurrentRes))
            if root.left == None and root.right == None:
                if currentSum == target:
                    self.res.append([item for item in self.CurrentRes])
                    # print("found: ", self.res)                    

            if root.left != None:
                findTarget(root.left, currentSum)
            if root.right != None:
                findTarget(root.right, currentSum)
            
            self.CurrentRes.pop()
            currentSum -= root.val
        
        if root != None:
            findTarget(root, 0)

        return self.res
    
test = Solution()
tree = [1,2,"null",3]
target = 5
root = createTreeNodeByLayerSeq(tree)
print(test.pathSum(root, target))