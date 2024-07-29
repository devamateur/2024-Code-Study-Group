# 참고: https://velog.io/@kimdukbae/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Floyd-Warshall-Algorithm
# 다익스트라: 정해진 출발 지점에서 최단 경로를 구하는 경우에 사용
# 플로이드 워셜: 모든 출발 지점에서 최단 경로를 구해야 하는 경우 사용
    # 거쳐가는 노드를 기준으로 최단 거리 갱신
class Solution:
    def floyd_warshall(self):
        INF = int(1e9)         # 10억

        # N: 회사(노드)의 개수, M: 경로(엣지)의 개수
        N, M = map(int, input().split())
        graph = [[INF]*(N+1) for _ in range(N+1)]        # 노드별 최단거리를 저장하는 N*N 2차원 리스트

        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    graph[i][j] = 0        # 자기 자신과의 거리는 0

        # 두 노드의 거리
        for _ in range(M):
            a, b = map(int, input().split())
            graph[a][b] = 1
            graph[b][a] = 1

        # X: 최종 도착지점, K: 경유지
        X, K = map(int, input().split())

        for k in range(1, N+1):
            for a in range(1, N+1):
                for b in range(1, N+1):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])        # a -> b와 a -> k -> b 경로 중 최소를 택함

        dist = graph[1][K] + graph[K][X]

        print(dist) if dist < INF else print(-1)         # 갈 수 없는 경로인 경우 dist가 INF보다 커지므로 dist<INF로 비교해야 하는 것 주의

s = Solution()
s.floyd_warshall()