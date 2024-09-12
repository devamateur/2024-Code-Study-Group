from collections import deque
class Solution:
    def visit(self):
        # N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
        N, M, K, X = map(int, input().split())
        
        edges = [[] for _ in range(N+1)]            # 도로 정보 저장
        distance = [-1]*(N+1)                  # 도로별 최단거리 저장
        distance[X] = 0                        # 출발 도시의 거리는 0으로 설정
        
        # 도로 정보 저장
        # a, b가 연결되어 있을 경우, a번 인덱스에 b 저장
        for _ in range(M):
            a, b = map(int, input().split())
            edges[a].append(b)
        
        q = deque([X])           # 데크
        
        while q:
            node = q.popleft()         # 데크에서 왼쪽 노드를 꺼냄

            # 현재 노드와 연결된 다른 노드 확인
            for next_node in edges[node]:
                if distance[next_node] == -1:         # 연결된 노드의 최단 거리가 설정되지 않았을 경우
                    distance[next_node] = distance[node] + 1          # 현재 노드와 연결
                    q.append(next_node)                    # 다음에 방문할 노드로 데크에 추가

        # 최단 거리 리스트에 거리가 K인 노드가 있으면
        if K in distance:
            for i in range(1, N+1):
                if distance[i] == K:
                    print(i)         # 해당 노드 프린트
        else:
            print(-1)

        '''
        dfs로는 풀 수 없는 문제...
        시작점 X가 주어질 때, X에서 갈 수 있는 모든 노드들을 다 확인하고 다음 경로를 봐야하므로
        def dfs(a, b, count):
            if count > K:
                return

            if count == K:
                nodes.append(b)
                return nodes

            for j in range(1, N+1):
                if a != j and b != j and not visited[j] and edges[b][j] == 1:
                    dfs(b, j, count+1)
                    visited[j] = True


        for j in range(1, N+1):
            if X != j and edges[X][j] == 1:
                visited[X] = True
                dfs(X, j, 1)
        
        if not nodes:
            print(-1)

        else:
            for node in nodes:
                print(node)'''

s = Solution()
s.visit()