class Solution:
    ''' 
    풀이 시간: 45분
    기존에 풀었던 그래프 문제들은 union-find를 이용해 트리를 만드는 문제였는데
    이 문제는 union-find를 이용해 두 노드간의 연결 여부를 파악하는 문제라는 점에서 차이가 있는 것 같다.

    노드들 간의 연결 정보가 N*N 행렬로 주어지기 때문에, 
    행렬을 입력받을 때 연결된 노드면 union 연산을 수행하면 된다.
    '''
    def make_plan(self):
        # find: 현재 노드의 부모를 찾음
        def find_parent(p, node):
            if p[node] != node:
                p[node] = find_parent(p, p[node])
            return p[node]
        
        # union: 부모가 다른 두 노드를 합침 (두 노드의 부모를 같은 노드로 갱신)
        def union(p, a, b):
            a_p = find_parent(p, a)
            b_p = find_parent(p, b)

            if a_p < b_p:
                p[b_p] = a_p
            else:
                p[a_p] = b_p
            return p
        
        # N: 여행지(전체 노드) 수, M: 도시(방문할 노드)의 수
        N, M = map(int, input().split())

        parent = [i for i in range(N+1)]

        # N*N 행렬 - 여행지 연결 정보
        edges = []  

        for i in range(N):
            edges.append(list(map(int, input().split())))

            for j in range(N):
                if i != j and edges[i][j] == 1:      # 서로 다른 두 노드가 연결되어 있으면 union
                    union(parent, i+1, j+1)
        
        # 여행계획 - 방문할 도시 정보
        plans = list(map(int, input().split()))
        
        ## union 결과값을 이용해 노드의 연결 여부 파악
        result = True
        for i in range(len(plans)-1):
            # 두 노드의 부모가 같으면, 연결된 것이므로 계속
            if find_parent(parent, plans[i]) == find_parent(parent, plans[i+1]):
                continue
            else:      # 두 노드의 부모가 다르면, 두 노드가 연결되지 않았다는 것이므로 break
                result = False
                break

        if result:     
            print('YES')
        else:
            print('NO')

s = Solution()
s.make_plan()