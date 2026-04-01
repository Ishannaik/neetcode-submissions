# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []
        def dfs(node, result):
            if not node:
                result.append(None)
                return None
            result.append(node.val)
            left = dfs(node.left, result)
            right = dfs(node.right, result)
            
        dfs(p, p_list)
        dfs(q, q_list)
        return p_list == q_list
