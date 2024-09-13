'''
🍪문제 번호 :
13장 DFS/BFS - 17 : 경재적 전염
https://www.acmicpc.net/problem/18405

🍈문제 정의 :
NXN크기의 시험관에 K가지 바이러스가 존재한다. S초가 지난 후 (X,Y)에 존재하는 바이러스의 종류(번호)를 출력하기

🍊풀이 시간 :
25분(시간초과)

🍒풀이 방법 :
dfs함수와 virus(1초기준 바이러스 퍼지는 함수)를 활용함
바이러스 번호가 작은순으로 맵 전체를 훝는 코드를 작성했지만 시간초과..
해설지를 확인해보니 deque를 활용

#solution
1) 입력과 동시에 해당 행의 (바이러스 번호, 시간, x, y)값을 변수리스트에 입력
2) 바이러스 번호를 기준으로 리스트 정렬 후 데큐에 입력
3) 데큐를 while로 반복

내 코드는 바이러스 번호기준으로 전체를 훝는 코드
solution은 방문하지 않은 위치에 넣어지는 바이러스 번호를 데큐에 넣어서 훝는 코드
데큐에는 1-2-3-1-2-3 순으로 넣어질테니 꼬이는 부분도 없음

'''
import sys
# sys.setrecursionlimit(10**9)

N,K = map(int,sys.stdin.readline().split()) #
graph = []
visited = [[False]*N for _ in range(N)]

for _ in range(N):
    graph +=list(map(int,sys.stdin.readline().split())),

S,X,Y = map(int,sys.stdin.readline().split())

# 1초기준 바이러스 퍼지기
def virus(x, y,virus_num):
    visited[x][y] = True    # 방문처리
    dist = [(1,0),(0,1),(-1,0),(0,-1)]          # 한번 상하좌우 움직임
    
    for dx,dy in dist :
        mx = x+dx
        my = y+dy
        if mx < 0 or mx > N-1 or my<0 or my > N-1 or visited[mx][my]:
            # 맵을 벗어나거나, 방문한 기록이 있다면 pass
            continue
        
        visited[mx][my] = True  # 방문처리
        graph[mx][my] = virus_num  # 바이러스 설정
    
    return

def dfs(s):
    if s == 0 :
        return
    
    for virus_num in range(1,K+1):
        for i in range(N) :
            for j in range(N):
                if not visited[i][j] and graph[i][j] ==virus_num:
                    virus(i,j,virus_num)
    
    s -=1
    dfs(s)

    return

dfs(S)
print(graph[X-1][Y-1])

