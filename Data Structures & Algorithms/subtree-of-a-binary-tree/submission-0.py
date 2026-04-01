# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            res1 = []
            res2 = []
            def dfs(node, res):
                if not node:
                    res.append(None)
                    return
                res.append(node.val)
                dfs(node.left, res)
                dfs(node.right, res)
            dfs(p, res1)
            dfs(q, res2)
            return res1 == res2
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
