import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for x, y, z in times:
            graph[x].append((y, z))

        min_heap = [(0, k)]         # (비용, 노드)
        distance = collections.defaultdict(list)

        while min_heap:       # 우선순위 큐
            time, node = heapq.heappop(min_heap)       # 큐에서 time이 가장 작은 노드를 꺼냄

            if node not in distance:      # 해당 노드를 방문한 적 없으면
                distance[node] = time     # 현재 경로에 추가

                for y, w in graph[node]:        # 해당 노드와 연결된 다른 노드를 방문
                    new_time = time+w           # 현재 경로의 time 갱신
                    heapq.heappush(min_heap, (new_time, y))

        if len(distance) == n:
            return max(distance.values())
        return -1