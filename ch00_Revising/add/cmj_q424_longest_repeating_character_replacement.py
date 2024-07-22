
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 딕셔너리를 미리 만들고 for문을 돌아야하는 줄 알았는데 for문 돌면서 딕셔너리를 갱신해야 함
        # 그리고, 직접 알파벳을 바꾸는 연산을 구현할 필요가 없음..
        
        left = 0
        freq = {}
        maxlen = 0        

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

            cur_window = i-left+1            # 지금 보고있는 윈도우

            if cur_window - max(freq.values()) <= k:  
                maxlen = max(maxlen, cur_window)
            else:
                freq[s[left]] -= 1
                left += 1

        return maxlen