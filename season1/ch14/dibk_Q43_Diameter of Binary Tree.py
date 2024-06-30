'''
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/description/
[time] 
[문제] 이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력
[풀이방식]
- 
'''
#failed
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        print('left : ',root.left)
        print('right : ',root.right)  
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        self.longest = max(self.longest, left,right)

        return self.longest+1

#solution
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest