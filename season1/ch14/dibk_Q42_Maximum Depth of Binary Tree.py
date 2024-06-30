'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
[time] failed
[문제]  
[풀이방식]
- 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0

        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1

        return max(left,right)