import math
import collections

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = collections.defaultdict(float)

        for i, (x, y) in enumerate(points):
            dist[i] = math.sqrt(x**2 + y**2)         # {인덱스: 원점과의 거리} 저장

        dist = dict(sorted(dist.items(), key=lambda x:x[1]))          # 가까운 거리순으로 정렬

        count = 0
        
        # 원점과의 거리가 가까운 지점 k개를 결과에 추가
        result = []
        for idx, distance in dist.items():
            result.append(points[idx])            
            count += 1
            if count == k:
                break

        return result