'''
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

[time] 15m but failed
[문제] 입력된 이진트리가 모든 노드의 서브 트리 간의 높이 차이가 1이하인 것을 판단하라.
[풀이방식]
- depth
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def function(root):
            if not root : return 1, True

            left, left_bool = function(root.left)
            right, right_bool = function(root.right)

            if abs(left-right)<2 :
                if left >= right :
                    return left+1 , True
                else :
                    return right+1, True
            else :
                return None, False
        
        _,bool_ = function(root)
        return bool_