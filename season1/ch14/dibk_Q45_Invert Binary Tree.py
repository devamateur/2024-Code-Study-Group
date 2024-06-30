'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/description/

[time] 4m
[문제] 중앙을 기준으로 이진 트리를 반전시키는 문제
[풀이방식]
- 직관적으로 문제를 해결함 : 좌우를 바꿔주면 됨.
- 마지막 리프노드까지 내려가서 return 해주고, 각 좌우를 바꾸면 됨.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root : return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root