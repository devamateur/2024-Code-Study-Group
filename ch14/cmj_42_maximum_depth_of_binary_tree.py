# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, count):
            if not node:
                return count
            
            left_depth = dfs(node.left, count+1)       # 왼쪽 서브트리
            right_depth = dfs(node.right, count+1)     # 오른쪽 서브트리
            
            return max(left_depth, right_depth)         # 최대 깊이

        result = dfs(root, 0)

        return result