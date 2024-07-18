'''
🍪문제 번호 :
704. Binary Search
https://leetcode.com/problems/binary-search/description/

🍈문제 정의 :
nums 리스트(오름차순 정렬되어 있는) 안에 target값이 있는 인덱스 구하기

🍊풀이 시간 :
10분

🍒풀이 방법 :
nums 리스트는 이미 정렬되어 있으므로 이진탐색 알고리즘 사용해야 함.
while문의 start,end 조건 주의하기(<=,<)


'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end :
            mid = (start+end)//2
            if nums[mid]== target :
                return mid
            
            elif nums[mid] > target :
                end = mid-1
            
            elif nums[mid] < target :
                start = mid+1

        return -1