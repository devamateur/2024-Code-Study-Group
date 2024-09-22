# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

'''

def solution(key, lock):
    answer = False
    
    M = len(key)        # 키 리스트의 크기
    rotate = [0, 90, 180, 270]          # 회전 각도

    # 이동 벡터
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
        
    new_key = [[0]*M for _ in range(M)]
    
    for angle in rotate:
        # 회전..
        visited = [[False]*M for _ in range(M)]
        count = 0
        if angle != 0:
            for i in range(M):
                for j in range(M):
                    new_key[j][M-1-i] = key[i][j]

        
        # 이동...
        for i in range(M):
            for j in range(M):
                if new_key[i][j] == 1:
                    for k in range(4):            # 상하좌우로 이동
                        new_x = i+dx[k] 
                        new_y = j+dy[k]
                        
                        # 값 갱신
                        new_key[new_x][new_y] = 1
                        new_key[i][j] = 0

                        # 이동 전 값 저장
                        prev_x = new_x
                        prev_y = new_y

                        # 현재 방향으로 리스트 경계까지 쭉 이동
                        while new_x > 0 or new_x < M or new_y > 0 or new_y < M:
                            new_x += dx[k]
                            new_y += dy[k]
                            if new_x < 0 or new_x > M-1 or new_y < 0 or new_y > M-1:
                                break
                            new_key[new_x][new_y] = 1
                            new_key[prev_x][prev_y] = 0
                            prev_x = new_x
                            prev_y = new_y


                if new_key[i][j] + lock[i][j] == 1:       # 같은 위치의 key와 lock을 더해서 1이 되면 카운트
                    count += 1

            if count == M*M:         # 카운트값이 key 리스트의 크기와 같아지면 True
                answer = True

    return answer
'''