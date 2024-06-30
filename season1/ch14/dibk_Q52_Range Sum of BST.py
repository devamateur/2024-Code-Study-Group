'''
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/description/

[time] 10m
[문제] 이진트리가 주어졌을 때 low이상 high이하의 값을 지닌 노드의 합을 구하기
[Note]
- root의 값이 low이상 high이하인 값일때만 result에 값 누적하고 각 left,right를 재귀하기
'''
class Solution:
    result = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root : return 

        if root.val >= low and root.val <=high :
            self.result +=root.val
        
        self.rangeSumBST(root.left,low,high)
        self.rangeSumBST(root.right,low,high)

        return self.result