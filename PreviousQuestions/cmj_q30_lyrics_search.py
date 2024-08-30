'''
    브루트 포스 -> 시간초과
def solution(words, queries):
    answer = [0] * len(queries)
    
    for i, q in enumerate(queries):
        ends = False             # 쿼리가 접두사(fro??), 접미사(????o)인지 표시
        current = ""           # 현재 쿼리에서 ?는 0으로 변환한 문자열 
        for char in q:
            current += char if char.isalpha() else "0"
        
        if current[0].isdigit():       # 쿼리의 시작이 숫자면 쿼리가 접미사임
            ends = True              # 접미사 표시
        current = current.replace('0', '')          # 0 삭제
        
        for j, w in enumerate(words):
            # 쿼리와 단어의 길이가 다르면 패스
            if len(q) != len(w): continue
            
            # 검색 쿼리와 매치된 단어
            if ends and w.endswith(current):       # 현재 쿼리가 접미사고 단어가 쿼리로 끝남
                answer[i] += 1                  
            elif not ends and w.startswith(current):      # 현재 쿼리가 접두사고 단어가 쿼리로 시작
                answer[i] += 1
    
    return answer

'''