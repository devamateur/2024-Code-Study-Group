'''
783. Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

[time] 25m
[문제] 두 노드 간 값의 차이가 가장 작은 노드의 값 차이를 출력하기
[Note]
- 
'''
class Solution:
    def makelist(self,root:Optional[TreeNode]) -> list :
        q = [root]
        result = []
        while q :
            node = q.pop(0)

            if node :
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)

        result.sort()
        return result

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        rootList = self.makelist(root)
        ans = 100000
        
        for idx in range(1,len(rootList)) :
            ans = min(ans, rootList[idx]-rootList[idx-1])
        
        return ans

'''
failed
root =[90,69,null,49,89,null,52]
Output : 3
Expected : 1 >> 90-89

class Solution:
    result = 100000
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root : return

        if root.left :
            left = root.val- root.left.val
        else :
            left = self.result

        if root.right :
            right = root.right.val - root.val
        else :
            right = self.result

        self.result = min(self.result,left,right)

        self.minDiffInBST(root.left)
        self.minDiffInBST(root.right)

        return self.result
'''