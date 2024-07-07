# 최소 칸의 개수 구하기
# 0: 괴물이 있는 칸, 1: 괴물이 없는 칸
class Solution():
    visited = []
    result = 40000  # 입력 크기 N*M이 최대 200*200이므로

    def escape_maze(self):
        N, M = map(int, input().split())

        maps = []

        for i in range(N):
            maps.append(list(map(int, input())))

        self.visited = [[False]*M for i in range(N)]


        def dfs(i, j, count):
            if i<0 or i > N-1 or j<0 or j>M-1 or maps[i][j] == 0 or self.visited[i][j]:
                return
            
            if i == N - 1 and j == M - 1:
                self.result = min(self.result, count)
                return self.result
            
            self.visited[i][j] = True
                        
            dfs(i+1, j, count+1)
            dfs(i-1, j, count+1)
            dfs(i, j+1, count+1)
            dfs(i, j-1, count+1)

            self.visited[i][j] = False   # 백트래킹


        dfs(0, 0, 1)

        print(self.result)

solution = Solution()
solution.escape_maze()