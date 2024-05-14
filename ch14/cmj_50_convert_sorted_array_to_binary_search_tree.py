# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        mid = len(nums)//2           # 루트의 위치

        if not nums:
            return None
        
        root = TreeNode(nums[mid])

        left = self.sortedArrayToBST(nums[:mid])            # 왼쪽 서브트리
        right = self.sortedArrayToBST(nums[mid+1:])         # 오른쪽 서브트리
        
        root.left = left         
        root.right = right
            
        return root