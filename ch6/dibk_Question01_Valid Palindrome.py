import re
class Solution :
    def isPalindrome1(self, s: str ) -> bool :
        '''
        - 정규표현식 사용하기 않기
        - 문자열 길이의 반 크기만큼만 비교하여 bool 처리하기
        '''
        
        # 입력값의 영문자와 숫자만(isalnum), 대소문자 구분x(lower) 
        s_list = list(filter(str.isalnum,s.lower()))
        s_size = len(s_list)
        s_half = s_size//2
        
        for i in range(s_half) :
            if s_list[i] != s_list[s_size-1-i] :
                return False
        return True
    
    def isPalindrome2(self, s: str ) -> bool :
        '''
        - 정규 표현식 사용하기
        '''
        re_s = re.sub('[^a-zA-Z0-9]','',s.lower())
        s_half = len(re_s)//2
        return re_s[:s_half] == re_s[:-s_half:-1]

"""

# Note - 정규 표현식 사용하기
- [^a-zA-Z0-9] : 숫자, 문자를 제외한 문자       result : aba
- \W : 숫자,_(언더바)를 제외한 문자             result : ab_a
example_string = 'ab_a'

# Note - Deque
- 리스트의 pop(0), O(n)
- Deque의 popleft(), O(1)

* Deque 
- 스택과 큐 기능을 모두 가진 객체, 양쪽에 출입구를 가짐.
from collections import deque
strs : deque = deque('dibk')
strs
>> deque(['d','i','b','k'])
        
"""
            