'''
🍪문제 번호 :
17장 최단경로 - 37번 플로이드
https://www.acmicpc.net/problem/11404

🍈문제 정의 :
N개의 도시가 있고 한 도시에서 출발하여 다른 도시에 도착하는 m개 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.
모든 도시 쌍에 대해서 A도시에서 B도시로 가는데 필요한 비용의 최솟값을 구하기.

🍊풀이 시간 :
failed

🍒풀이 방법 :
- 출력 결과물을 봐도 문제 이해가 가지 않았음
- 플로이드 와샬 알고리즘 문제에 해당됨.
    - 모든 점에서 모든 정점으로의 최단 경로를 구하고 싶을 때 사용됨.
    - vs 다익스트라: 가장 적은 비용을 하나씩 선택
    - vs 플로이드 와샬 : 거쳐가는 정점을 기준으로 최단 거리를 구함
    *https://blog.naver.com/ndb796/221234427842

- "시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다." > 노드 사이 거리 중 최소값 추가

'''

import sys
INF = int(1e9)

N = int(sys.stdin.readline("도시의 수").rstrip())
M = int(sys.stdin.readline("버스의 수").rstrip())

graph = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j :
            graph[i][j] =0

for _ in range(M) :
    a,b,cost = map(int,sys.stdin.readline().split())
    
    if graph[a][b] > cost :
        graph[a][b] = cost

#  "시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다." : 확인
for row2 in range(1,N + 1):                               # row2 : (거쳐가는 노드)
    for row1 in range(1,N + 1):
        for col in range(1,N + 1):
            cost[row1][col] = min(cost[row1][col],cost[row1][row2] + cost[row2][row1])