'''
🍪문제 번호 :
*슬라이딩윈도우
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/

🍈문제 정의 :
m,n길이의 문자열 s,t가 있는데, t의 문자열을 모두 포함하는 s의 최소 substring을 구하기. 없다면 빈값"" 반환하기.
*substring : 빈값이 없는 연속적인 문자시퀀스.


🍊풀이 시간 :
failed

🍒풀이 방법 :
t문자열 딕셔너리를 생성(need)하고, missing(t의 문자열 크기)를 정의한다.
s를 순회하는 인덱스 right와, 후발확인을 위한 left인덱스를 활용하여 딕셔너리 복원작업으로 풀이를 진행한다.

'''
# solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)           # 필요한 문자와 문자 갯수 
        missing = len(t)                        # 최소 윈도우
        left = start = end = 0                  # 포인터 초기화

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):     # 인덱스를 1부터 시작하게 함.
            if need[char] > 0 :
                # if need[char] >0 이면(t의 문자열이면) missing을 -1
                missing -=1           
            need[char] -= 1                     # 문자의 빈도 -1 ::  need에 없는 문자는 음수부터 정의됨.
                                                # missing == 0되기 전까지 need에 t가 없는 문자들은 음수로 계속 추가됨. or 반복의 경우 계속 음수가 됨.

            # 필요 문자가 0이면, s문자열에서 t문자열에 해당되는 것을 모두 발견했다는 의미
            if missing == 0:
                while left < right and need[s[left]] < 0:       # left를 right이 움직인 만큼 이동하는데(missing이 0이 된 위치까지), need의 문자가 음수라면, 복구해주고, left를 right까지 이동
                    need[s[left]] += 1                          # 없는 문자들은 0으로 복구되고, 있는 문자는 원래 빈도만큼 복구
                    left += 1

                if not end or right - left <= end - start:      # end가 움직이지 않았거나(0), start,end의 위치가 더 높은 경우 swipe
                    start, end = left, right
                    
                need[s[left]] += 1                  # 위 while문에서 left가 right랑 같은 경우는 실행하지 않았기 때문에.
                missing += 1
                left += 1
        return s[start:end]

# failed
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) <= len(t) : return ""

        # 연산에 사용될 deque : 해당 문자가 있는 인덱스값(위치) 저장
        tmp = deque()
        window_size = len(t)
        t_dict = collections.Counter(t)

        # 1. t사이즈만큼(최소window크기) s를 순회하여 해당 문자의 인덱스 위치 찾기
        for idx in range(window_size):
            if s[idx] in t :
                tmp.append(idx)

        # tmp[0]]은 t 문자가 있는 s의 제일 앞의 위치
        # 2.
        result = []

        while tmp or end < len(s) :
            
            if tmp :
                start = tmp.popleft()
                end = start+window_size

            if end >= len(s):
                if not tmp : break
                start = tmp.popleft()
                end = start+windowsize 
                continue

            print(s[start:end])
            if collections.Counter(s[start:end])&t_dict == t_dict: 
                result += s[start:end],
                print('result')

                for idx in range(start+1,end) :
                    if s[idx] in t :
                        tmp.append(idx)

                start = tmp.popleft()
                end = start+window_size  
            else :
                end+=1

        return result
