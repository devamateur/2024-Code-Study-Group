class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
        l = 0     # 왼쪽 포인터
        freq = {}
        maxlen = 0

        for r in range(len(s)):
            # 딕셔너리 초기화
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            # 현재 부분 문자열의 길이를 구하고, 최대 빈도수를 뺀다. 이 값이 K 이하인지 확인한다.
            cur_len = r - l + 1
            # cur_len - max(freq.values()): 윈도우 크기 - 가장 흔한 알파벳의 개수 = 교체해야 할 알파벳 개수
            if cur_len - max(freq.values()) <= k:  # K 이하로 문자를 교체할 수 있으면, 최대 길이 갱신
                maxlen = max(maxlen, cur_len)
            else:                                 # K보다 많이 교체한 경우, 슬라이딩 윈도우를 오른쪽으로 이동
                freq[s[l]] -= 1                   # 왼쪽 포인터의 문자의 빈도를 감소시키고, 포인터를 증가시킨다.
                l += 1
            
        return maxlen