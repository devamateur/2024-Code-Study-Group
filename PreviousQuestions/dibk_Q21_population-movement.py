'''
🍪문제 번호 :
13장 DFS/BFS - 21 : 인구 이동
https://www.acmicpc.net/problem/16234

🍈문제 정의 :
NxN맵 크기의 땅이 있고, 각 행열에는 각 나라의 인구수가 입력되어 있다.
하루동안 조건에 맞게 인구는 이동하는데 인구이동이 며칠 동안 발생하는 지 구하기

🍊풀이 시간 :
30분(failed)

🍒풀이 방법 :
실패한 풀이)
모든맵을 확인하는 run함수(백트래킹)과 run함수에서 상하좌우로 확인하는 check함수를 활용하여 풀이하려고 함
- run함수로 맵 전체를 훝으며 확인하고, check함수로 1번 실행시 인구이동으로 묶이는 값을 구하려고 함.
- 하지만 30분동안 구현했더니, 인구이동으로 구해지는 값 뿐만 아니라 값이 변하는 맵의 위치도 중요하다는 것을 나중에 알게됨

solution)
process함수는 1번 실행시 움직이는 나라를 확인하는 함수, While True로 맵을 순회
특이점은 if index == n * n를 통해서 while문 빠져나옴.

'''
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    print("union :",x,y,nx,ny,index)
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]            # while문을 통해서 항상 초기화 됨
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우  -- 이중for문을 순회했는데, index가 NXN값가 같으면 모든 맵을 확인했다는 의미임으로 while문 나오기
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)


"""
import sys
from collections import deque

N,L,R =map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph +=list(map(int,sys.stdin.readline().split())),

visited = [[False]*N for _ in range(N)]
result = 0

def run():
    
    resum,recount = 0,0
    for i in range(N):
        for j in range(N):
            output,bin = check(i,j)
            resum +=output
            recount +=bin
    
    return

def check(x,y):
    dist = [(1,0),(0,1),(-1,0),(0,-1)]
    visit = 0
    count = 0
    
    for mx,my in dist:
        dx = x+mx
        dy = y+my
        
        if dx < 0 or dx >= N or dy < 0 or dy >= N or visited[dx][dy]:
            continue
        
        if abs(graph[x][y] - graph[dx][dy]) >=L and abs(graph[x][y] - graph[dx][dy]) <=R :
            visited[dx][dy] = True
            visit+=graph[dx][dy]
            count +=1
    
    if count > 0 :
        if not visited[x][y] :
            visited[x][y] = True
            visit +=graph[x][y]
            count +=1
        return visit,count
    else :
        return 0,0
"""