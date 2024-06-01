'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/

[time]
[문제] 부분 문자열이 포한된 최소 윈도우 문제로, t의 모든 문자열이 포한된 s의 부분 문자열을 구하기.
[풀이방식] :
- 투 포인터, 슬라이딩 윈도우 최적화 :
    - 투 포인터 사용시, O(n^2) -> O(n)
    - 오른쪽으로 이동하는 슬라이딩 윈도우 : s에서 이동할 위치를 t의 문자열이 있는 위치에서 시작

'''
# solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = collections.Counter(t)         # t의 빈도 딕셔너리
        min_window = len(t)                     # 최소 윈도우 길이
        left = start = end = 0                  # 초기화 : start와 end는 값을 기록하고, left는 움직이는 변수

        # 오른쪽 포인터 이동                     # 오른쪽으로 윈도우 크기를 키워나감.
        for right, char in enumerate(s, 1):     # 1-idx부터 시작 >>>>>>>> 0인덱스를 1로 시작하게 함.
            min_window -= t_dict[char] > 0           # 해당 문자가 딕셔너리에 존재하면, min_window에서 해당 크기만큼 빼기
            t_dict[char] -= 1                   ###(포인트) t에 없는 문자열은 -1로 정의됨.

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if min_window == 0:                             # 찾을 문자를 다 찾은 경우,
                while left < right and t_dict[s[left]] < 0:     # t_dict[s[left]] 해당 문자열의 값이 음수 :: t에 없는 문자열
                    t_dict[s[left]] += 1                        # t에 없는 문자열이 중복이어도 -1로 정의되었기 때문에 +- 0값이 됨
                    left += 1                                   # 왼쪽 포인터를 오른쪽으로 이동 ( left<right )

                if not end or right - left <= end - start:      # right-left값이 작으면 start,end값 저장
                    start, end = left, right
                t_dict[s[left]] += 1                            # 다시 복원
                min_window += 1                                     
                left += 1
                
        return s[start:end]


# failed
import re
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t : return s
        if len(s) <= len(t) : return ""
        if t in s : return t
        
        t_dict = {}
        indices = []

        for ch in t :
            if ch not in t_dict :
                t_dict[ch] = 0
            t_dict[ch]+=1

            if s.find(ch) == -1 : return ""

            for idx, val in enumerate(s):
                if val == ch:
                    indices.append(idx)
        indices.sort()

        end,start = indices.pop(),indices.pop()
        
        while indices :
            if end-start+1 < len(t) :
                start = indices.pop()
            elif start==0 :
                return s
            else :
                return s[start-1:end+1]