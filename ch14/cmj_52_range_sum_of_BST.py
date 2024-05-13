class Solution:
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return None
            
            if low <= node.val and node.val <= high:
                self.result += node.val
            
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

            return self.result
        
        dfs(root)
        return self.result