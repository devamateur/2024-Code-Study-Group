import collections
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 원점에서 가까운 점 K개 구하기

        distance = collections.defaultdict(float)
        for i, (x, y) in enumerate(points):
            loc = math.sqrt(x**2 + y**2)
            distance[i] = loc      # 딕셔너리에 {인덱스: 원점과의 거리} 저장
        
        distance = dict(sorted(distance.items(), key=lambda x:x[1]))        # 거리가 가까운 순으로 정렬

        result = []
        for i, loc in distance.items():
            result.append(points[i])
            k -= 1
            if k == 0:
                break
        
        return result
