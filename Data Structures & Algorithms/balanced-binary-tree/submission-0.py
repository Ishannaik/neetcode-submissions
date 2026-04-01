# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return 0
            print(node) #ROOT HERE
            left = dfs(node.left)
            right = dfs(node.right)
            if left is False or right is False:
                return False
            if abs(left-right)>1:
                return False
            return 1 + max(left,right)
        if dfs(root):
            return True
        return False