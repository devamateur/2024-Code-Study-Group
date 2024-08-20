class Solution:
    def remove_road(self):
        '''
            일부 간선을 비활성화하여 절약할 수 있는 최대금액 구하기
            절약 최대 금액 = 전체 비용 합 - 최소 스패닝 트리의 비용 합
            -> 최소 스패닝 트리 만들기 => 크루스칼 알고리즘

            답이 계속 책이랑 다르게 나와서 계속 고치고 지피티한테도 물어봤는데
            그냥 테스트케이스를 잘못 입력했었다... 너무 화나요
        '''

        # union-find
        def find_parent(p, node):
            if p[node] != node:
                p[node] = find_parent(p, p[node])
            return p[node]
        
        def union(p, a, b):
            a = find_parent(p, a)
            b = find_parent(p, b)

            if a<b:
                p[b] = a
            else:
                p[a] = b

        # N: 집(노드), M: 도로(간선)
        N, M = map(int, input().split())
        graph = []
        parent = [i for i in range(N)]

        for _ in range(M):
            x, y, cost = map(int, input().split())        # x, y: 두 집, cost: 두 집 사이 거리(비용)
            graph.append((cost, x, y))


        # 노드별 비용이 작은순으로 정렬
        # ex) 0번 노드에 비용이 7인 간선, 5인 간선이 있으면 -> 5, 7로 정렬
        graph.sort()

        # 간선을 제거하기 전 전체 비용
        total_cost = 0
        kruskal_sum = 0
        for cost, x, y in graph:
            total_cost += cost
            if find_parent(parent, x) != find_parent(parent, y):
                union(parent, x, y)
                kruskal_sum += cost

        print(total_cost - kruskal_sum)


s = Solution()
s.remove_road()