from collections import defaultdict

def solution(s):
    answer = len(s)
    
    compressed = ""    
    
    for i in range(1, len(s)//2+1):        
        prev = s[:i]
        count = 1
        compressed = ""
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:         # 같은 문자가 나오면 카운트 증가
                count += 1
            else:                  # 다른 문자가 나오면, 현재까지 문자를 압축
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+i]
                count = 1
                
        # 남아있는 문자열 처리 -> 문자열 단위가 커지는 경우 남는 문자열이 생김 
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(len(compressed), answer)
    
    return answer