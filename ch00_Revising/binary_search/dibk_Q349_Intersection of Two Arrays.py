'''
🍪문제 번호 :
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/description/

🍈문제 정의 :
두 리스트의 교집합을 구하기

🍊풀이 시간 :
1분

🍒풀이 방법 :
set함수와 교집합함수 활용

'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1)&set(nums2)