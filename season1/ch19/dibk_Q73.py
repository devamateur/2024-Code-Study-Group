'''
393. UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/description/

[time] failed
[문제] 입력값이 utf-8이 맞는 지 확인하기.
[풀이방식]
- failedㅠ

rule :
1바이트: 0xxxxxxx
2바이트:110xxxxx 10xxxxxx
3바이트:1110xxxx 10xxxxxx 10xxxxxx
4 바이트:11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
'''

# solution
# ex) data = [235,140,4]
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True