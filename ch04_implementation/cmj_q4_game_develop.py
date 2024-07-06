N, M = map(int, input().split())

y, x, direction = map(int, input().split())       # 좌표, 현재 바라보고 있는 방향

game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

# 방향
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
dir = [0, 3, 2, 1]  # 회전 방향: 북, 서, 남, 동

# 이동방향: 북, 서, 남, 동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

noway = 0
# 1. 현재 위치에서 왼쪽 방향부터 차례대로 갈 곳을 정함

# 시작 방향 기준 왼쪽 방향의 인덱스 가져옴
idx = dir.index(direction)+1

while True:
    # 2. 왼쪽에 아직 가보지 않은 칸이 있으면, 왼쪽으로 회전해서 왼쪽으로 한 칸 전진
        # 가보지 않은 칸이 없으면, 왼쪽으로 회전만 수행
    # 방향 별 왼쪽
    # 북쪽: 왼쪽, 동쪽: 위, 남쪽: 오른쪽, 서쪽: 아래

    game_map[y][x] = 2             # 방문한 칸은 2로 표시
    new_x = x + dx[idx]
    new_y = y + dy[idx]

    if game_map[new_y][new_x] == 0:        # 방문하지 않은 칸
        x = new_x
        y = new_y
        game_map[new_y][new_x] = 2
        noway = 0
    else:                   # 방문한 칸이면 카운트
        noway += 1

    # 방향 인덱스 설정
    if idx < 3:
        idx += 1
    else:
        idx = 0

    # 3. 네 방향 모두 가본 칸 or 바다인 경우 현재 방향을 유지한채 한칸 뒤로 가고 1단계로 돌아감
        # (단, 이때 뒤쪽 방향이 바다여서 뒤로 갈 수 없는 경우에는 움직임을 멈춤)
    # 네 방향 모두 갈 수 없는 경우
    if noway == 4:
        new_x = x - dx[idx]
        new_y = y - dy[idx]

        # 뒤로 갈 수 있다면 이동하기
        if game_map[new_y][new_x] == 0:
            x = new_x
            y = new_y
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        noway = 0

# 2인 칸의 갯수 리턴
print(sum(item.count(2) for item in game_map))


