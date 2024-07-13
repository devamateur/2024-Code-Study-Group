'''
🍪문제 번호 :
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

🍈문제 정의 :
두 문자열(s,t)가 애너그램이면 truem 아니면 False를 반환하기

🍊풀이 시간 :
3분

🍒풀이 방법 :
1) 딕셔너리 사용 O(N)
2) 정렬 사용 O(NlogN)

other) count함수와 set

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for ch in s :
            if ch not in dict_s.keys():
                dict_s[ch] = 0
            dict_s[ch] +=1

        dict_t = {}
        for ch in t :
            if ch not in dict_t.keys():
                dict_t[ch] = 0
            dict_t[ch] +=1
        
        return dict_t == dict_s

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    
# other
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {v: s.count(v) for v in set(s)}
        d2 = {v: t.count(v) for v in set(t)}
        
        return d1 == d2

