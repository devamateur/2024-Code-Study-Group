class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and matrix[0][0] != target:
            return False

        # 오른쪽 위에서부터 값을 찾음
        col = len(matrix[0])-1
        row = 0

        while row < len(matrix) and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:         # target보다 작아지면 밑으로 이동
                row += 1
            else:                             # target보다 크면 왼쪽으로 이동
                col -= 1
        
        return False