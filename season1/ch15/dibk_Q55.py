'''
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

[time] 15m
[문제] k번째로 큰 요소를 구하기.(sort함수 사용불가)
[풀이방식]
- heapq를 구현하려고 했지만 실패
- heapq 라이브러리 활용
- 
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -n)

        for _ in range(k):
            result = heapq.heappop(h)

        return -result


# failed
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        root = TreeNode(nums[0])
        q = [root]
        idx = 1
        
        while idx < len(nums)-1 :
            node = q.pop(0)

            if nums[idx] > node.val :
                node,node.left = TreeNode(nums[idx]),node
            else :
                node.left = TreeNode(nums[idx])
            idx +=1

            if nums[idx] < node.left.val :
                node.right,node.left = node.left, TreeNode(nums[idx])
            else :
                node.right = TreeNode(nums[idx])
            idx +=1

            q.append(node)
        

        return 

# 시간 초과...
# 34 / 41 testcases passed
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = [nums.pop()]

        while nums :
            num = nums.pop()

            for idx in range(len(result)):
                if result[idx] <= num :
                    result = result[:idx]+[num]+result[idx:]
                    break
            
            else :
                result.append(num)
        
        return result[k-1]