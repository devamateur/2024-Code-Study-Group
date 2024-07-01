'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/description/

[문제] 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라.

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def move(y,x) :
            if (x<0 or x>=len(grid[0])) or (y<0 or y>=len(grid)) or grid[y][x] !='1':
                return

            grid[y][x] ='0'     # visited 처리
            move(y,x+1)         # col 열(좌우)로 +1
            move(y,x-1)         
            move(y+1,x)         # row 행(위아래)으로 +1
            move(y-1,x)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    move(row,col)
                    count+=1
        
        return count