'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/description/

[time] 10m
[문제] 좌표값들 중 원점에서 가장 가까운 값들을 k번째까지 리턴하기
[풀이방식] : heap사용
- 원점에서 거리값과 좌표값을 heap에 입력
- k번 순회하여 k개의 가까운 좌표값 추출
- 답지랑 똑같다.

'''
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x,y in points :
            result = x**2 + y**2
            heapq.heappush(distances,[result,[x,y]])
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(distances)[1])
        
        return result
    
# other solution : heap을 사용하지 않고 sort

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x,y in points:
            dist = x**2 + y**2
            distances.append((dist, [x,y]))
        
        kClosestDistances = sorted(distances, key=lambda x: x[0])[:k]   # x[0] dist값 기준
        return [x[1] for x in kClosestDistances]                        # x[1] 좌표값