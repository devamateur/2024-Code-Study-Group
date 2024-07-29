import heapq

class Solution:
    def dijkstra(self):
        INF = int(1e9)

        # N: 노드 개수, M: 간선 수, C: 시작 노드
        N, M, C = map(int, input().split())
        graph = [[] for i in range(N+1)]           # 각 노드 연결 정보를 저장
        distance = [INF]*(N+1)                # 현재까지의 최단 경로 저장

        for _ in range(M):
            node1, node2, cost = map(int, input().split())
            graph[node1].append((node2, cost))
        #print(graph)

        # 우선순위 큐
        q = [] 
        heapq.heappush(q, (0, C))       ### 우선순위 큐에 (거리, 노드) 형태로 저장. 이렇게하면 거리가 가까운 노드부터 큐에서 제거가능
        distance[C] = 0         # 현재 거리 표시

        while q:
            dist, node = heapq.heappop(q)
            
            # 이미 방문한 경우
            if dist > distance[node]:
                continue
            
            # 연결되어 있는 노드 정보 확인
            for next_node, next_dist in graph[node]:
                # 연결된 노드까지의 거리
                cost = dist + next_dist

                # 새로운 거리가 해당 노드까지의 최단 거리보다 작으면, 최단 거리 갱신
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))

        # city_count: 메시지를 전송할 수 있는 도시(노드)의 수
        # arrival_time: 도시가 모두 메시지를 받는 데 걸리는 시간
        city_count = 0
        arrival_time = 0

        for i in range(len(distance)):
            if distance[i] != INF:
                city_count += 1
                arrival_time = max(arrival_time, distance[i])
        
        if city_count != 0:
            print(city_count-1, arrival_time)         # city_count-1: 출발 도시 제외
        else:
            print("최단 경로 없음!")
        

s = Solution()
s.dijkstra()