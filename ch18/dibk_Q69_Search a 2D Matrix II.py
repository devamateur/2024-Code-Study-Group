'''
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

[time] 7m
[문제] mXn 배열에서 target값을 찾기(각 행렬은 오름차순)
[풀이방식] :
- 이중 for문으로 해결
- 답지의 경우) row = 0, col = 맨 끝부터 시작해서 값 비교하기
'''

class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])) :
                if matrix[row][col] == target :
                    return True
        
        return False
    

# solution
class Solution:
    def searchMatrix(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로
            elif target > matrix[row][col]:
                row += 1
        return False