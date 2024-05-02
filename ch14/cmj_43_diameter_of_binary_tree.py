# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1         ### 존재하지 않는 노드의 리턴값 -1

            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)

            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest
    
    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        # 최대 지름을 저장할 변수
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0          ###  존재하지 않는 노드의 리턴값 0, 즉 엣지수가 0임을 나타냄
            
            left = dfs(node.left)          
            right = dfs(node.right)
            
            
            # 최대 지름 업데이트
            self.max_diameter = max(self.max_diameter, left + right)      ### 현재 노드의 엣지수 = left + right
            
            # 현재 노드의 깊이 반환
            return max(left, right) + 1
        
        # 루트 노드에서 깊이 계산을 시작
        dfs(root)
        
        return self.max_diameter