class Solution:
    def ranking(self):
        '''
            임의의 두 학생간의 상대 순위만 쌍으로 주어질 때,
            성적을 확실히 알 수 있는 학생의 수를 구하는 문제
            
            성적을 확실히 알 수 있음 
            -> 모든 노드가 해당 노드와 직간접적으로 연결되어 있다 (이걸 생각을 못했다)
            => 즉, 거쳐가는 노드를 고려해야 하는 최단 경로 문제
            다익스트라: 시작 노드가 정해져있을 때의 최단 경로 ex) A에서 시작하는 최단경로
            플로이드-워셜: 모든 노드를 고려한 최단 경로 
            => 이 문제는 플로이드-워셜을 이용한 최단경로 문제다
            
        '''
        # N: 학생 수, M: 학생 성적 비교(간선)
        N, M = map(int, input().split())

        graph = [[float("inf")]*(N+1) for _ in range(N+1)]         # 초기 거리는 inf(무한대)로 설정

        for i in range(N+1):
            for j in range(N+1):
                if i == j:
                    graph[i][j] = 0             # 자기 자신과의 거리는 0
        
        for _ in range(M):
            a, b = map(int, input().split())
            graph[a][b] = 1                # 연결된 노드의 거리는 1
        
        
        ## 플로이드-워셜
        # 노드 a-b 사이의 거리를 구하는데, 거쳐가는 중간 노드를 고려
        # k노드를 거쳐갈 때와 거쳐가지 않을 때 중 최소를 택함
        for k in range(1, N+1):
            for a in range(1, N+1):
                for b in range(1, N+1):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

        # 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
        result = 0
        for i in range(1, N+1):
            count = 0        # 노드 i와 나머지 노드들과의 연결을 카운트
            for j in range(1, N+1):
                # i와 j 노드가 연결되어 있으면 카운트 증가
                if graph[i][j] != float("inf") or graph[j][i] != float("inf"):
                    count += 1
            if count == N:    # 카운트가 N이 되면, 즉 i와 다른 노드들이 모두 연결되어 있으면 result 증가
                result += 1
        print(result)

s = Solution()
s.ranking()