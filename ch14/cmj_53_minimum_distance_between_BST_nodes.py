class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []
        def inorder(root):          # 중위순회를 이용해 값을 오름차순으로 정렬
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)

        inorder(root)

        result = nums[1]-nums[0]
        for i in range(2, len(nums)):
            result = min(result, nums[i]-nums[i-1])

        return result
    
    '''39 / 49 testcases passed
    result = 1000000
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, root):
            if not node:
                return None
            
            if parent and node:
                self.result = min(self.result, abs(parent.val-node.val))
                self.result = min(self.result, abs(root.val-node.val))
            left = dfs(node.left, node, root)
            right = dfs(node.right, node, root)
            
            return self.result

        dfs(root, None, root)
        return self.result
    '''