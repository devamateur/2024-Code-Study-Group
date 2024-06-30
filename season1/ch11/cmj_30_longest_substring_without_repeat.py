class Solution:
    # 방법 1: dictionary를 이용하는 방법
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        
        start = 0
        max_length = 0

        for i in range(len(s)):
            if s[i] in my_dict and start <= my_dict[s[i]]:      # 기존에 본 알파벳이 등장하면 start 위치 갱신
                start = my_dict[s[i]] + 1
            else:
                max_length = max(max_length, i-start+1)         # longest substring 길이 계산
            my_dict[s[i]] = i             # {알파벳: 위치} 형태로 저장
        
        return max_length

    # 방법2: set을 이용하는 방법
    def usingSet(self, s: str) -> int:
        char_set = set()
        start = 0
        max_length = 0

        for i in range(len(s)):
            while s[i] in char_set:                # 기존에 본 알파벳이 등장하는 동안
                char_set.remove(s[start])          # 현재 알파벳이 아닌 처음 set에 저장한 알파벳 제거
                start += 1                         # start 위치 갱신
            char_set.add(s[i])
            max_length = max(max_length, i - start + 1)

        return max_length