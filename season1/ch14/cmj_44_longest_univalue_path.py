# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0          ### 같은 값이 아니면 해당 경로로 가지 않음
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0         ###

            self.result = max(self.result, left + right)       # 현재 노드에서 왼쪽 자식과 오른쪽 자식을 택함

            return max(left, right) 

        dfs(root)
        return self.result