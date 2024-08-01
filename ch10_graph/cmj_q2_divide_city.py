import sys
input = sys.stdin.readline                       #### 입력

class Solution:
    def divide(self):
        ''' 
        크루스칼 알고리즘: https://chanhuiseok.github.io/posts/algo-33/
        N: 집(노드), M: 길(간선)

        2개의 마을로 분리 -> 2개의 스패닝 트리

        마을 안에 있는 임의의 두 집 사이에 항상 경로가 존재해야 함 -> 스패닝 트리
        길의 유지비 합을 최소로 함 -> 최소 스패닝 트리 -=> 크루스칼 알고리즘
        분리된 두 마을 사이 간선은 없앰

        즉, 2개의 최소 스패닝 트리를 만들기 위해서는
        크루스칼 알고리즘으로 최소 스패닝 트리를 만들고,
        트리에서 유지비가 가장 높은 간선을 제거하면 됨 '''

        N, M = map(int, input().split())
        graph = []
        parent = [i for i in range(N+1)]

        for _ in range(M):
            # a: 집1, b: 집2, c: 유지비(cost)
            a, b, c = map(int, input().split())
            graph.append((c, a, b))         # cost 순으로 정렬해야 하므로 cost를 앞에 저장

        # 유지비 기준 오름차순 정렬
        graph.sort()
        
        def find_parent(p: list, a):
            if p[a] != a:
                p[a] = find_parent(p, p[a])        #### 경로 압축, 루트를 현재 노드의 부모로 설정 설정
            return p[a]
        
        def union(p: list, a, b):
            a_p = find_parent(p, a)
            b_p = find_parent(p, b)

            if a_p < b_p:
                p[b_p] = a_p
            else:
                p[a_p] = b_p

            return p

        result = 0
        last = 0
        for i in range(len(graph)):
            if find_parent(parent, graph[i][1]) != find_parent(parent, graph[i][2]):
                parent = union(parent, graph[i][1], graph[i][2])

                result += graph[i][0]             # 유지비 합계
                last = graph[i][0]             # 유지비 max값
        
        print(result - last)              # 유지비 합계 - 유지비 max  = 2개 스패닝 트리에서 최소 유지비

s = Solution()
s.divide()