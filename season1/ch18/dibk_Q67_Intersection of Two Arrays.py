'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

[time] 2m
[문제] 두 개의 정수 배열 num1, num2에서 공통된 원소를 찾기
[풀이방식] :
- 리스트를 set으로 변경 후, 교집합 함수 사용해서 리턴

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)