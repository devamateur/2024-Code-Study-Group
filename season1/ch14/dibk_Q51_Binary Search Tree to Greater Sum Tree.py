'''
1038. Binary Search Tree to Greater Sum Tree
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

[time] failed
[문제] 이진검색트리 root를 현재값보다 더 큰 값을 가진 노드의 합으로 반환하기
[Note]
- root.right는 root.val보다 항상 큰 값이기 때문에 먼저 재귀확인.
- result는 누적값으로 순회하며 값을 더해감.
- root.val에 누적된 값으로 복사해주고 root.left를 재귀해야 right-root-left순으로 값을 누적해갈 수 있음.
'''

class Solution:
    result = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root :
            self.bstToGst(root.right)
            self.result +=root.val
            root.val = self.result
            self.bstToGst(root.left)
        
        return root