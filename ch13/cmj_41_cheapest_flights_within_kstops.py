import sys
import heapq
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        weight = [(sys.maxsize, k)] * n      # 현재 경로까지의 (비용, step)을 저장하는 리스트

        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    new_price = price + w
                    if new_price < weight[v][0] or k-1 >= weight[v][1]:        ##### 
                        weight[v] = (new_price, k-1)
                        heapq.heappush(Q, (new_price, v, k - 1))
        return -1