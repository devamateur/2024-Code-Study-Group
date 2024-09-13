'''
🍪문제 번호 :
13장 DFS/BFS - 16 : 연구소
https://www.acmicpc.net/problem/18352

🍈문제 정의 :
N×M인 공간에서 (빈 칸 0, 벽 1, 바이러스 2)가 있다. 여기에 벽 3개를 세운 뒤, 바이러스가 퍼질 수 없는 안전 영역의 크기 최대값을 구하기

🍊풀이 시간 :
failed

🍒풀이 방법 :
문제점) 벽 3개를 어디에 설치할 지(눈으로 볼 때는 알겠는데 시스템으로 어떻게 찾아낼지,,)
- 1을 기준으로 벽세우기
- 2를 기준으로 벽세우기

앞 이론문제에서 "음료수 얼려 먹기"가 생각나는 문제
(같은 번호끼리 뭉쳐서 계산하는 부분)

solution)
미친문제,, 실행할 때 안터지는 게 신기
1) dfs함수 : 맵을 순회하며 모든 가정을 확인하는 main 함수
2) virus 함수 : 벽3개 설치 완료 되었을 경우, 바이러스가 퍼지게 하는 함수
3) score 함수 : 바이러스 퍼진 후, 안전 영역 확인하는 함수

'''
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)