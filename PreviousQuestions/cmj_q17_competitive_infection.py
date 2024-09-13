from collections import deque
class Solution:
    def spread(self):
        '''
            N*N 시험관에 바이러스가 K번까지 있을 때, S초후 (X, Y)좌표 시험관에 있는 바이러스 구하기
            바이러스는 상하좌우로 전염되며, 번호가 작은 바이러스부터 전염
            어떤 칸에 바이러스가 이미 있는 경우, 다른 바이러스가 그 칸에 전염될 수 없음
        '''
        # N: 시험관 크기(N*N), K: 바이러스 번호(1~K번)
        N, K = map(int, input().split())

        maps = []
        virus = []
        for i in range(N):
            maps.append(list(map(int, input().split())))

        # S: 초, XY: 시험관 좌표
        S, X, Y = map(int, input().split())

        for i in range(N):
            for j in range(N):
                if maps[i][j] != 0:
                    virus.append((maps[i][j], 0, i, j))        # 바이러스 번호, 시간, 좌표

        virus.sort()           ### 바이러스 번호 순으로 방문해야 하므로
        q = deque(virus)
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        while q:
            v_num, sec, min_x, min_y = q.popleft()
            
            if sec == S:             ### 
                break

            for i in range(4):
                new_x = min_x + dx[i]
                new_y = min_y + dy[i]

                # 경계 체크
                if new_x < 0 or new_x > N-1 or new_y < 0 or new_y > N-1: continue

                # 바이러스가 전염되지 않은 칸일 때에만 전염
                if maps[new_x][new_y] == 0:
                    maps[new_x][new_y] = v_num
                    q.append((v_num, sec + 1, new_x, new_y))

        print(maps[X-1][Y-1])

s = Solution()
s.spread()