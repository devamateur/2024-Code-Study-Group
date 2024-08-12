'''
🍪문제 번호 :
18장 그래프 이론 - 44번 행성 터널
https://www.acmicpc.net/problem/2887

🍈문제 정의 :
3차원 공간에 N개의 행성으로 이뤄진 우주가 있다. 행성을 연결하는 터널을 총 N-1개 건설하여 모든 행성이 연결되게 하려고 하는데, 최소 연결 비용을 구하기

입력 :
N(행성 갯수)
x,y,x(각 행성의 좌표)

🍊풀이 시간 :
failed

🍒풀이 방법 :
- 모든 행성이 연결된다, 최소 비용 : 크루스칼 알고리즘?

# failed
1.모든 행성끼리의 거리비용을 저장하기(maxtrix)
2.최소거리(비용)을 기준으로 정렬하여 행성 연결하기(서로소 집합 알고리즘) 활용(union, find)

>> x,y,z를 하나의 좌표로 인식하여 distance를 구하려고 했는데, x,y,z를 각각의 점으로 저장하여 거리를 구했어야 했다.

'''

class Solution :
    
    def planets(self):
        import sys

        # 함수
        def find(x):
            if parent[x] !=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union_(a,b):
            aa = find(a)
            bb = find(b)
            if aa<bb:
                parent[b]=aa
            else :
                parent[a]=bb

        # 입력
        N = int(sys.stdin.readline().rstrip())
        parent = [i for i in range(N+1)]

        xlist = []
        ylist = []
        zlist = []

        for i in range(1, N + 1):
            x,y,z = map(int,sys.stdin.readline().split())
            xlist += [x,i],
            ylist += [y,i],
            zlist += [z,i],

        xlist.sort()
        ylist.sort()
        zlist.sort()

        edges = []
        
        for i in range(n - 1):
        # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
            edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
            edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
            edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
        
        # 간선을 비용순으로 정렬
        edges.sort()

        result = 0
        # 간선을 하나씩 확인하며
        for edge in edges:
            cost, a, b = edge
            # 사이클이 발생하지 않는 경우에만 집합에 포함
            if find(a) != find(b):
                union_(a, b)
                result += cost

        print(result)
    
test = Solution()
test.gate()



# 작성 중단 코드
'''
import sys

# 함수
def find(x):
    if parent[x] !=x:
        parent[x] = find(parent[x])
    return parent[x]

def union_(a,b):
    aa = find(a)
    bb = find(b)
    if aa<bb:
        parent[b]=aa
    else :
        parent[a]=bb

# 입력
N = int(sys.stdin.readline().rstrip())
parent = [i for i in range(N+1)]

planets = []
for _ in range(N) :
    planets += list(map(int,sys.stdin.readline().split())),

distance_maxtrix = [[0]*N for i in range(N)]
for idx in range(len(planets)) :
    for jdx in range(idx+1,len(planets)) :
        x,y,z = [abs(x-y) for x,y in zip(planets[idx],planets[jdx])]
        result = x**2+y**2+z**2
        distance_maxtrix[idx][jdx] = result
        
'''