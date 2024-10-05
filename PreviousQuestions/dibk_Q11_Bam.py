'''
🍪문제 번호 :
12장 구현 - 11 : 뱀
https://www.acmicpc.net/problem/3190

🍈문제 정의 :
Dummy라는 뱀 길이가 커지는 게임. NXN맵에서 진행되고 사과를 먹으면 뱀 길이가 길어짐.
게임이 몇 초에 끝나는지 구하기

🍊풀이 시간 :
failed

🍒풀이 방법 :
https://data-flower.tistory.com/65
참고함

- 데큐 활용하는 게 익숙하지 않음.
    - 뱀의 현재 위치를 데큐에 넣기
- 방향을 리스트 활용해서 움직이는 방법 기억해두기

'''
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[0]*N for _ in range(N)]

# 사과 횟수
K = int(sys.stdin.readline().rstrip())
# 사과 좌표
for _ in range(K):
    row,col =map(int,sys.stdin.readline().split())
    # 사과 표시 1
    graph[row-1][col-1] = 1

# 뱀 방향 회전
L = int(sys.stdin.readline().rstrip())
change_snake = []
for _ in range(L):
    X,C =map(str,sys.stdin.readline().split())
    second = int(X)
    change_snake +=(second,C),

# 위(0), 오른쪽(1), 아래(2), 왼쪽(3)
direction = [(-1,0),(0,1),(1,0),(0,-1)]

snake = deque()
snake.append([0,0]) # 현재 뱀이 있는 자리 표시, 뱀이 움직일때마다 pop,push
cx,cy = 0,0     # 현재 뱀 머리 위치

d = 1    # 방향(1) 오른쪽
time = 0   # 게임 시간

trigger = False
for x,c in change_snake:
    # 뱀 머리 방향 횟수만큼 for문 순회
    # x : 시간(초), c: 방향
    start = time +1
    for _ in range(start, x+1):
        time +=1
        mx = cx + direction[d][0]
        my = cy + direction[d][1]
        
        if mx < 0 or mx >=N or my <0 or my >=N or (mx,my) in snake :
            # 맵 밖으로 나간다면, 움직인 위치mx,my에 snake가 있다면 충돌
            trigger = True
            break
        
        if graph[mx][my] == 1:
            graph[mx][my] = 0   # 사과 먹기
        else :
            snake.popleft()     # 뱀 꼬리 위치 빼기
        
        cx,cy = mx,my
        snake +=(cx,cy),     # 뱀 현재 머리 위치 추가하기
    
    # 빠져나오기
    if trigger :
        break
    # 빠져나오지 않고 다음 머리 방향으로 이동시
    if c == 'D' :
        d +=1
        if d >=4 :
            d = 0
    else:
        # c == 'L'
        d -=1
        if d < 0 :
            d = 3

print(time)