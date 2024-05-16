import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify(nums)
        nums_size = len(nums)
        count = 0
        result = 0

        while nums:
            n = heapq.heappop(nums)
            count += 1
            if count == nums_size - k+1:
                result = n
                break

        return result