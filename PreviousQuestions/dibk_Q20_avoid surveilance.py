'''
🍪문제 번호 :
13장 DFS/BFS - 20 : 감시 피하기
https://www.acmicpc.net/problem/18428

🍈문제 정의 :
NXN맵이 존재하고, 선생님(T), 학생(S), 장애물(O)이 위치한다.
장애물을 3개 설치하여 모든 학생이 선생님들의 감시를 피할 수 있도록 출력하기.(출력값이 yes or no)

🍊풀이 시간 :
40분(백준에서 틀림)

🍒풀이 방법 :
연구소 문제와 유사한 것 같다. 하지만 이 문제는 DFS보다 백드래킹 문제로 보임

1) T를 기준으로 상하좌우 확인하기
- S가 발견되면 전 칸에 O심어두기
- 전 칸이 없다면 return No
- o가 3개 이상 심어야한다면 return No

'''
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []

obj = 3
q = deque()

for i in range(N):
    nodes =list(map(str,sys.stdin.readline().split()))
    
    for j in range(N) :
        if nodes[j] == "T":
            q.append((i,j))
    
    graph +=nodes,

def run(x,y,dist):
    dx = x +dist[0]
    dy = y + dist[1]
    
    if dx < 0 or dx >= N or dy < 0 or dy >= N :
        return False
    
    if graph[dx][dy] == "O" :
        return False
    
    if graph[dx][dy] == "S" :
        return x,y

    return run(dx,dy,dist)

trigger = True
while obj :
    x,y = q.popleft()
    
    dist = [(1,0),(0,1),(-1,0),(0,-1)]
    
    for d in dist :
        result = run(x,y,d)
        if result and result[0] == x and result[1] == y :
            trigger = False
            break
        elif result:
            graph[x][y] = "O"
            obj -=1
    
    if not trigger :
        break

if trigger :
    print("YES")
else :
    print("NO")
