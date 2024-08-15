import heapq
class Solution:
    def find_spot(self):
        # N: 헛간 개수, M: 통로(간선)
        N, M = map(int, input().split())

        # 1번 헛간으로 부터 가장 먼 헛간 구하기
        # 숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간의 개수 구하기
        INF = int(1e9)
        graph = [[INF]*(N+1) for _ in range(N+1)]
        distance = [INF]*(N+1)

        for _ in range(M):
            a, b = map(int, input().split())
            graph[a][b] = 1        # 두 노드가 연결되어 있음을 표시, 양방향
            graph[b][a] = 1

        q = [(0, 1)]       # 거리, 헛간 번호
        distance[1] = 0        # 현재 노드의 거리를 0으로 갱신

        while q:
            dist, curr = heapq.heappop(q)

            # 현재 노드 a의 최단거리보다 더 크면 넘어감
            if distance[curr] < dist:
                continue
            
            # curr와 연결된 노드 확인
            for next_node, next_dist in enumerate(graph[curr]):
                if next_dist == INF:        # 갈 수 없는 노드는 넘어감
                    continue

                # 연결된 노드까지의 거리
                new_dist = dist + next_dist

                if new_dist < distance[next_node]:         # new_dist가 기존 next_node의 최단 거리보다 작으면, 갱신
                    distance[next_node] = new_dist
                    heapq.heappush(q, (new_dist, next_node))          # 큐에 다음에 방문할 노드로 추가
        print(distance)
        
        # 숨어야 하는 헛간 = 노드 1에서 가장 먼 헛간
        # 근데, 거리가 같은 헛간이 여러개면 가장 작은 번호 출력

        max_idx = 0        # 헛간 번호
        max_dist = 0       # 헛간까지의 거리
        count = 1         # 거리가 같은 헛간의 개수, 자기 자신도 포함해야 하므로 1로 초기화
        for i in range(1, len(distance)):
            if distance[i] == INF:
                continue
            
            if max_dist < distance[i]:
                count = 1          # 더 큰 값이 나타나면 count값 초기화
                max_idx = i
                max_dist = distance[i]

            elif max_dist == distance[i]:
                count += 1
        print(max_idx, max_dist, count)
s = Solution()
s.find_spot()
