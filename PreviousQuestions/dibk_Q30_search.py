'''
🍪문제 번호 :
15장 이진탐색 - 30 : 가사 검색
https://school.programmers.co.kr/learn/courses/30/lessons/60060

🍈문제 정의 :
failed

🍊풀이 시간 :
14분

🍒풀이 방법 :
re 라이브러리 사용 :: 정확성  테스트, 효율성  테스트(실패,실패,실패,성공,성공)
pattern = re.compile("정규표현식$")
1) pattern.findall(text)      :: 한 문장("~~")에 대해 매칭되는 것 추출 : 리스트형태로 반환
2) list(filter(pattern.match,list))    :: 리스트에서 매칭되는 것 추출 : 리스트 형태

'''
import re
def solution(words, queries):
    answer = []
    
    for p in queries:
        #
        # if p[0] == '?' :
        #     query = p.replace('?','.') +'$'
        # else :
        #     # p[-1] == '?'
        #     query = '^' + p.replace('?','.')
        
        query = '^' + p.replace('?','.') +'$'               # ex) "????o"     ->     ^....o$
        pattern = re.compile(query)
        output = list(filter(pattern.match,words))          # ex) ["frodo","kakao"]
        answer += len(output),
    
    return answer

# solution
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드 카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드 카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer