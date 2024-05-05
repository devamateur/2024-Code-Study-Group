class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return max(left, right)+1
        
        return dfs(root) != -1

    ''' 이진트리 최대 깊이 풀었던 방식으로 시도했으나 실패...
        219 / 228 testcases passed
    result = []
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = []

        def dfs(node, count):
            if not node:
                self.result.append(count)
                return count
            
            left_depth = dfs(node.left, count+1)       # 왼쪽 서브트리
            right_depth = dfs(node.right, count+1)     # 오른쪽 서브트리

            return max(left_depth, right_depth)

        dfs(root, 0)
        
        diff = max(self.result) - min(self.result)
        return diff <= 1'''