'''
🍪문제 번호 :
75. Sort Colors
https://leetcode.com/problems/sort-colors/description/

🍈문제 정의 :
red,white,blue 객체로 이뤄진 nums 배열이 있다. 해당 배열을 같은 색체끼리 인접하도록 정렬하기
0(red), 1(white), 2(blue)
*in-place : 별도의 사본을 생성하지 않고 그 자체에서 작업

🍊풀이 시간 :
1분

🍒풀이 방법 :
1) sort함수 사용.
2) O(N) 시간 복잡도의 코드 구현 : count함수 사용
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        zero, one, two = nums.count(0),nums.count(1),nums.count(2)
        nums[:] = [0]*zero + [1]*one + [2]*two