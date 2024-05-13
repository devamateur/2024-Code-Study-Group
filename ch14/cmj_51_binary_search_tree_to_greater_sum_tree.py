# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    node_sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):            
            if node:
                dfs(node.right)
                self.node_sum += node.val
                node.val = self.node_sum
                dfs(node.left)
            
        dfs(root)
        return root