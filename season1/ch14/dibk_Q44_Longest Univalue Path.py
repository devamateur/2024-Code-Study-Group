'''
687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/description/
[time] 
[문제] 동일한 값을 지닌 가장 긴 경로 찾기 --> 노드 값이 같은 노드끼리 얼마나 이어져 있는지 뎁스 찾기
[풀이방식]
- 
'''
class Solution:
    longest = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node,parent):
            if not node : return 0

            left = dfs(node.left,node)
            right = dfs(node.right,node)
            self.longest = max(self.longest,left+right)

            if parent and node.val == parent.val :
                return max(left,right)+1
            return 0
        
        dfs(root,None)
        return self.longest



class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result