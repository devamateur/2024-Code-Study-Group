class Solution:
    def floyd(self):
        n = int(input())     # 도시 수
        m = int(input())     # 버스 수
        
        graph = [[float("inf")]*(n) for _ in range(n)]        # 모든 노드들간의 거리를 무한대값으로 설정정
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][j] = 0       # 자기 자신과의 거리는 0

        for _ in range(m):
            a, b, cost = map(int, input().split())
            
            graph[a-1][b-1] = min(cost, graph[a-1][b-1])      # 시작도시와 도착도시를 연결하는 간선은 1개 이상이므로 그 중 최소 비용을 저장

        ## 플로이드 워셜
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])    # i->j와 k를 거쳐서 가는 i->k->j 중 최소를 택함
        
        # 결과 출력력
        for line in graph:
            for item in line:
                if item == float("inf"):       # 갈 수 없는 경로는 0으로 설정
                    item = 0
                print(item, end=' ')
            print()

s = Solution()
s.floyd()