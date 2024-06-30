'''
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

[time] failed
[문제] 리스트(배열)을 높이 균형 이진 탐색 트리로 변형하기
[Note]
- 상위 노드 찾는 방법 - 입력리스트의 중간 값 : len(nums)//2
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums : return None

        mid = len(nums)//2
        
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node