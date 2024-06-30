'''
617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/description/

[time] 15m
[문제] 두 이진트리를 병합하기(더하기)
[풀이방식]
- 두 이진트리 중 한 노드에 더한 값을 덮어씌우기(root1에 덮어씌움)
- 좌우노드 각자 리프노드까지 내려가고, 둘다 없거나 하나만 있을 때까지 내려감.
- root1에 값을 덮어씌운고(root1.left = left) root1.val + root2.val 연산 후 root1을 반환
'''
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2 : return root1 if root1 else root2 if root2 else None
        
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)

        root1.val += root2.val

        return root1

# 정리 전 코드
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2 : return 
        elif not root1 : return root2
        elif not root2 : return root1
        
        left = self.mergeTrees(root1.left,root2.left)
        right = self.mergeTrees(root1.right,root2.right)
        
        root1.left = left
        root1.right = right
        root1.val += root2.val

        return root1