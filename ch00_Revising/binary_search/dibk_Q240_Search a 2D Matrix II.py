'''
🍪문제 번호 :
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

🍈문제 정의 :
mXn 행렬에서 target값이 존재하는 지 확인하는 문제.
행렬은 오름차순으로 정렬되어 있음.

🍊풀이 시간 :
10분

🍒풀이 방법 :
배열의 0행의 큰값부터 값을 비교하며 target이 값보다 크면 행으로 움직이고 작으면 열을 움직이는 구조
while문의 조건을 row<=col이라고 아무생각 없이 작성했는데 이 부분 주의.

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = 0, len(matrix[0])-1

        while row < len(matrix) and col >=0 :
            
            if matrix[row][col] == target :
                return True

            elif matrix[row][col] > target :
                col -=1
            
            elif matrix[row][col] < target :
                row +=1
        
        return False