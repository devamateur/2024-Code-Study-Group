import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 필요한 문자가 모두 포함될때까지 오른쪽 포인터 확장
        for right, char in enumerate(s, 1):
            if need[char] > 0:       # missing -= need[char] > 0
                missing -= 1
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                # 문자가 필요한 것보다 더 많이 포함되어 있으면 왼쪽 포인터를 증가해서 윈도우 축소
                while left < right and need[s[left]] < 0: 
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                
                # 다음 반복 준비
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]

    # 너무 어려워요
    # 132 / 268 testcases passed
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(s) < len(t):    # s가 t보다 짧은 경우
            return ""
        if t in s:         # t가 그대로 들어있는 경우
            return t
            
        l, r = 0, len(t)-1
        w_count = 0
        result = ""
        for i in range(len(s)):
            for j in range(len(t)):
                # substring이 t와 같으면 리턴
                if s[l:r+1] == t:
                    return s[l:r+1]
                #print(s[l:r+1])

                # substring이 t와 같지 않을 때,
                if t[j] in s[l:r+1]:          # t의 문자가 substring에 있으면, 카운트 증가하고 포인터 확장
                    r += 1
                    w_count += 1
                else:                         # t의 문자가 없으면, 카운트 0으로 초기화하고 포인터 오른쪽으로 이동
                    w_count = 0
                    l += 1
                if w_count == len(t):         # 카운트가 t 길이와 같으면, substring이 t와 완전히 같지는 않지만 t를 포함             
                    result = s[l:r+1]
                    break
        
        # t를 포함하는 substring에서, t에 없는 문자 제거
        while result and result[0] not in t:
            result = result[1:]
        while result and result[-1] not in t:
            result = result[:-1]
        
        # t와 substring에 있는 문자의 개수가 다른 경우, substring에서 문자 제거
        # ex) t = "aba", result = "bbaa"
        i = 0
        while result:   
            if i >= len(result):
                break 
            if result[i] in t and result.count(result[i]) > t.count(result[i]):    
                result = result[:i] + result[i+1:]
            else:
                i += 1

        return result