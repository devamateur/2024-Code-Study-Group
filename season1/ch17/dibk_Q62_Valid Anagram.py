'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

[time] 3m
[문제] 두 문자열이 애나그램인지 확인하기
[풀이방식]
- 이게 되네?
- 딕셔너리끼리 비교 가능
- 답지 솔루션은 NlogN, but 큰 차이는 없는 것 같다.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for ch in s :
            if ch not in dict1.keys():
                dict1[ch]=0
            dict1[ch] +=1
        
        for ch in t :
            if ch not in dict2.keys():
                dict2[ch]=0
            dict2[ch] +=1
        
        return dict1==dict2
    
# solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)