from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        deq = deque()

        for i in range(len(nums)):
            # Deque의 앞에서 윈도우에 포함되지 않는 인덱스를 제거
            if deq and deq[0] < i - k + 1:          # i-k+1: 현재 슬라이딩 윈도우의 left
                deq.popleft()

            # Deque의 뒤에서 현재 값보다 작은 값들을 제거
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # 현재 인덱스를 deque에 추가
            deq.append(i)

            # 첫 윈도우가 완료된 이후부터 결과에 최대값을 추가
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result