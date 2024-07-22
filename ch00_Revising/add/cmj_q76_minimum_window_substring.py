from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)        # t의 문자 카운터
        missing = len(t)         # 필요한 문자 수
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0         # 현재 문자 char가 t에 있으면, missing 감소
            need[char] -= 1                 # 현재 문자 char의 카운트 감소

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:       # 해당 문자가 없으면
                    need[s[left]] += 1                          # 해당 문자 필요 카운트 증가
                    left += 1

                ### 최소 윈도우 갱신. 더 작은 크기의 윈도우를 찾으면 해당 윈도우로 갱신함
                ### if not end 조건은 end = 0이면 True (정수는 0일 때 False, 나머지는 True로 판단하므로)
                ### -> if end == 0으로 바꿔도 같은 결과가 나옴
                if not end or right - left <= end - start:    
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]