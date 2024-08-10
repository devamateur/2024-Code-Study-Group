import sys
input = sys.stdin.readline

class Solution:
    def connect(self):
        # 모든 행성을 연결하는 최소 비용 출력 -> 최소 스패닝 트리에서 비용의 합

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

        # N: 행성의 개수

        N = int(input())
        
        x_loc = []
        y_loc = []
        z_loc = []

        graph = []

        parent = [i for i in range(N)]
        
        
        for i in range(N):
            x, y, z = map(int, input().split())      # 각각 행성의 x, y, z 좌표
            
            # x, y, z 좌표를 따로 리스트에 저장
            x_loc.append((x, i))         # (좌표, 인덱스) 튜플로 저장
            y_loc.append((y, i))
            z_loc.append((z, i))
            
        # 오름차순 정렬 -> 뒤에 있는 원소가 무조건 앞에 있는 원소보다 크므로 절댓값 씌울 필요가 없어짐
        x_loc.sort()
        y_loc.sort()
        z_loc.sort()

        # print(x_loc)
        # print(y_loc)
        # print(z_loc)

        # 행성의 연결 비용 = min(|xa-xb|, |ya-xb|, |za-zb|) 라고 되어있는데
        # 왜 ya-yb를 추가하는지 모르겠다... |ya-xb|가 오타인건지
        for i in range(N-1):
            graph.append((x_loc[i+1][0] - x_loc[i][0], x_loc[i][1], x_loc[i+1][1]))
            graph.append((y_loc[i+1][0] - y_loc[i][0], y_loc[i][1], y_loc[i+1][1]))
            graph.append((z_loc[i+1][0] - z_loc[i][0], z_loc[i][1], z_loc[i+1][1]))
        
        # 그래프도 오름차순 정렬 -> 비용이 작은 노드부터 합친다
        graph.sort()

        result = 0
        for edge in graph:
            cost, a, b = edge

            if find_parent(parent, a) != find_parent(parent, b):
                union(parent, a, b)
                result += cost

        print(result)
s = Solution()
s.connect()