def solution(m, n, board):
    board = [list(x) for x in board]       # 2차원 배열로 변환

    while True:
        # 1) 일치 여부 판별
        matched = []              # 2*2 블록의 왼쪽 최상단 블록 저장
        for i in range(m - 1):
            for j in range(n - 1):
                if  board[i][j] != '#' and board[i][j] == board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j]:
                    matched.append([i, j])

        # 2) 일치한 위치 삭제
        # 여기서는 지워진 블록을 #로 표시
        for i, j in matched:
            board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = board[i + 1][j] = '#'

        ##### 3) 빈공간 블럭 처리
        # 제거된 블록 위에 있는 블록을 아래로 떨어뜨림
        for _ in range(m):             # 블록이 끝까지 떨어지도록 보장
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':           # 삭제된 블록
                        board[i + 1][j], board[i][j] = board[i][j], '#'              # 삭제된 블록과 현재 블록 값 교체

        if not matched:
            break
        
    return sum(x.count('#') for x in board)