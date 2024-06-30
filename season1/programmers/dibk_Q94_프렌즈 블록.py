'''
프렌즈 블록
https://school.programmers.co.kr/learn/courses/30/lessons/17679

[time] failed
[풀이방식] :

'''
# solution
def solution(m: int, n: int, board: List[str]) -> int:
    board = [list(x) for x in board]

    matched = True
    while matched:
        # 1) 일치 여부 판별
        matched = []
        for i in range(m - 1):                      # 행 이동(y)
            for j in range(n - 1):                  # 열 이동(x)
                # 상하좌우가 같고, '#'아 아니면 matched에 좌표 저장
                if board[i][j] == \
                        board[i][j + 1] == \
                        board[i + 1][j + 1] == \
                        board[i + 1][j] != '#':
                    matched.append([i, j])

        # 2) 일치한 위치 삭제
        # 해당 좌표만 순회
        for i, j in matched:
            board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = board[i + 1][j] = '#'

        # 3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':          # 다음행의 값이 '#'이면
                        board[i + 1][j], board[i][j] = board[i][j], '#'     # 다음행에 현재의 값 저장, 현재행에는 '#'

    return sum(x.count('#') for x in board)



# failed
# 풀이 방법 : 
# 4번의 board를 순회. 첫번째 순회할 때, 2X2블록이 같은 경우를 기록해둔다. 두번째 순회 때, 사라지는 블록 갯수를 카운트하고 사라지는 블록에 행의 위치를 바꿔서 재정립한다. 이후 반복
# 같은 문자 블록을 확인하는 함수 sameBlock()를 정의.
#   해당 좌표(위치)에서 '해당위치-오른쪽-아래-왼쪽'이 같은 문자일 경우 True이며, ground_map배열에 해당 위치들을 1로 바꿈
#   두번째 순회에서 1 카운트하기
#   이후 멘붕
def solution(m, n, board):
    move = [(1,0),(1,1),(0,1)]
    ground_map = [[0]*n for i in range(m)]
    gap_map = [[0]*n for i in range(m)]
    
    def sameBlock(x,y) :
        block = board[y][x]
        for x_,y_ in move:
            curx,cury = x+x_,y+y_
            if board[cury][curx]!=block:
                return False
        
        ground_map[y][x] = 1
        for x_,y_ in move:
            curx,cury = x+x_,y+y_
            ground_map[cury][curx] = 1
        return True
    
    # 첫번째 순회
    for i in range(m):
        for j in range(n):
            sameBlock(n,m)
    
    # 두번째 순회
    result = 0
    for i in range(m):
        result += ground_map[m].count(1)
        print(result)
        # 행(y)을 이동시키기 위해 gap을 구해야 하는데, 이동해야하는 좌표를 gap_map에 기록하려고 함.
        # 근데 그러려면 결국 전체 순회를 해야하는구나..