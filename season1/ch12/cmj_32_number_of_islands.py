class Solution:
    def dfs(self, grid: List[List[str]], visited: List[List[bool]], x: int, y: int, land_count: int):

        # base case
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):  # 경계값
            return

        if visited[x][y]:   # 방문여부
            return

        if grid[x][y] == "0":    # 물
            return 

        visited[x][y] = True
                    
        self.dfs(grid, visited, x+1, y, land_count)
        self.dfs(grid, visited, x-1, y, land_count)
        self.dfs(grid, visited, x, y+1, land_count)
        self.dfs(grid, visited, x, y-1, land_count)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        visited = [[False]*col_size for _ in range(row_size)]      # 2차원 리스트 초기화
        result = 0

        for i in range(row_size):
            for j in range(col_size):
                if not visited[i][j] and grid[i][j] == "1":
                    result += 1
                    self.dfs(grid, visited, i, j, 0)

        return result