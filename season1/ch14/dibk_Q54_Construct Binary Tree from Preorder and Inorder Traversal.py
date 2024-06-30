'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

[time] failed
[문제] 트리의 전위중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.
[Note]
- 전위순회(preorder)에서 메인이 되는 노드를 중위순회(inorder)에서 찾기
- (3)노드가 메인노드, 중위순회(inorder)에서 (3)의 위치인 (1)번 인덱스를 추출
    (3)노드가 메인노드 생성 : TreeNode(inorder[index]) ==== TreeNode(preorder.pop(0)) === TreeNode(3)
- (3)메인노드를 중심으로 left, right 순회하기
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder : return

        index = inorder.index(preorder.pop(0))  # preorder[0] : 3  전위순회(preorder)에서 메인이 되는 노드를 중위순회(inorder)에서 찾기
                                                # inoerder.index(3) : 1     
        node = TreeNode(inorder[index])         # (3)노드을 메인노드 생성 
        
        node.left = self.buildTree(preorder, inorder[0:index])      # preorder, inorder([9])
        node.right = self.buildTree(preorder, inorder[index + 1:])  # preorder, inorder([15,20,7])

        return node