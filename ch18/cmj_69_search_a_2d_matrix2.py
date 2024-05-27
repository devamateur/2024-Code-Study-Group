class Solution:
    # O(m+n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n=len(matrix), len(matrix[0])
        i, j=0, n-1      #### 오른쪽 위에서 시작

        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:       # 타겟보다 클 경우, 왼쪽으로 이동
                j-=1
            else:                           # 타겟보다 작을 경우, 아래 행으로 이동
                i+=1
        return False

    

''' 풀긴 풀었는데 40분 걸린 야매코드...   
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 1:
            if target in matrix[0]:
                return True
            return False

        left, right = 0, len(matrix[0])-1

        i=0
        while left <= right and i<len(matrix):
            mid = (left+right)//2
            curr = matrix[i][mid]

            if curr > target:
                right -= 1
            elif curr < target:
                left += 1
            else:
                return True

            if matrix[i][(left+right)//2] == target:
                return True
            if left >= len(matrix[0]) or right >= len(matrix[0]):
                left = 0
                right = len(matrix[0])-1
            if left == right:
                left = 0
                right = len(matrix[0])-1
                i += 1

        return False'''

