from collections import deque

class Solution:
    # ex) nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    # r=0, deq = [0], result = []
    # r=1, deq = [0] -> deq.pop() -> [] -> deq.append(r) -=> deq = [1]
    # r=2, deq = [1] -> deq.append(r) -=> deq=[1, 2], result = [3]
    # r=3, deq = [1, 2] -> deq.append(r) => deq=[1, 2, 3], result = [3, 3]
    # r=4, deq = [1, 2, 3] -> deq.popleft() -> deq=[2, 3] -> deq.pop()*2 -> deq[2] -> deq.append(r) => deq = [2, 4], result = [3, 3, 5]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        deq = deque()

        for r in range(len(nums)):
            # 윈도우 인덱스 관리
            # 윈도우 범위에 포함되지 않는 인덱스 제거
            # 현재 윈도우 범위 = r-k+1 ~ r
            if deq and deq[0] < r - k + 1:          # r-k+1: 현재 슬라이딩 윈도우의 left
                deq.popleft()

            # Deque에 현재 값보다 작은 값이 있는 동안 계속 제거
            # 현재 값보다 크거나 같은 값을 남김김
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # 현재 인덱스를 deque에 추가
            deq.append(r)

            # 첫 윈도우가 완료된 이후부터 결과에 최대값을 추가
            if r >= k - 1:
                result.append(nums[deq[0]])

        return result

    ''' 시간초과...
    데큐에 윈도우 크기만큼 원소를 넣고,
    max값을 result에 추가한 뒤 데큐에서 왼쪽 원소 제거

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k: 슬라이딩 윈도우 사이즈
        # 매번 슬라이딩 윈도우는 오른쪽으로 한 번 움직임

        ## 각 슬라이딩 윈도우에서 max값 구하기
        d = deque()

        r = 0    
        result = []

        while r < len(nums):
            d.append(nums[r])

            if len(d) == k:
                result.append(max(d))
                d.popleft()
                
            r += 1

        return result '''