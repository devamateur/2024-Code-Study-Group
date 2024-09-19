from collections import deque
class Solution:
    def move(self):
        '''
            더 이상 인구 이동이 없을때까지 아래 진행
            국경선을 공유하는 두 나라 (행 또는 열 인덱스 차이가 1)
            - 인구 차이가 L명 이상, R명 이하라면, 국경선을 오늘 하루 연다
            - 열어야하는 국경선이 모두 열렸다면 인구 이동 시작
            - 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 하루 동안은 연합이라고 함

            - 연합
            - 연합을 이루고 있는 각 칸의 인구수 = (연합의 인구수) // (연합을 이루고 있는 칸의 개수)
            - 연합을 해체하고 모든 국경선을 닫는다

            인구 이동이 며칠동안 발생하는지 구하기
        '''

        N, L, R = map(int, input().split())

        A = []

        for _ in range(N):
            A.append(list(map(int, input().split())))

        # 방향 벡터
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        # 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
        def process(x, y, index):
            # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
            united = []
            united.append((x, y))

            # 초기화
            q = deque()
            q.append((x, y))
            union[x][y] = index         # 연합 여부 표시
            summary = A[x][y]           # 현재 연합의 전체 인구 수
            count = 1                   # 현재 연합의 국가 수
            
            while q:
                x, y = q.popleft()
                # 현재 위치에서 4가지 방향을 확인하며
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 바로 옆에 있는 나라를 확인하여
                    if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                        # 인구수 차이 계산, L명 이상 R명 이하인지 확인
                        if L <= abs(A[nx][ny] - A[x][y]) <= R:
                            q.append((nx, ny))
                            # 연합에 추가하기
                            union[nx][ny] = index      # index: 연합 여부 표시, -1이 아니면 엽합임
                            summary += A[nx][ny]       # 연합 인구수에 더하기
                            count += 1                 # 연합 수 증가
                            united.append((nx, ny))    # 연합 목록에 추가

            # 연합 국가끼리 인구를 분배
            for i, j in united:
                A[i][j] = summary // count

        total_count = 0

        # 더 이상 인구 이동을 할 수 없을 때까지 반복
        while True:
            union = [[-1] * N for _ in range(N)]
            index = 0
            for i in range(N):
                for j in range(N):
                    if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                        process(i, j, index)
                        index += 1
            # 모든 인구 이동이 끝난 경우
            if index == N * N:
                break
            total_count += 1

        # 인구 이동 횟수 출력
        print(total_count)

'''        
        q = deque([[A[0][0], 0, 0], [A[0][1], 0, 1]])      # 0행 0열과 0행 1열 나라의 [인구수, 행, 열] 저장

        open_border = 0         # 제거한 국경선의 개수
        index = []              # 국경선을 제거한 나라들의 인덱스

        while q and len(q) >= 2:
            # 두 나라씩 인구수, 행, 열을 꺼냄
            country1, i, j = q.popleft()
            country2, k, l = q.popleft()

            if L <= abs(country1-country2) and abs(country1-country2) <= R:
                open_border += 1
                index.append([i, j, k, l])
            else:
            # 다음 노드를 어떻게 방문해야할지
            # 인구수 차이를 어떤식으로 계산해야할지 잘 모르겠음 -> 방향 벡터로 하면 되는거였다...
'''

s = Solution()
s.move()