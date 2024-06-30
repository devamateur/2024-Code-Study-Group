'''
다트 게임
https://school.programmers.co.kr/learn/courses/30/lessons/17682

[time] 1h
[풀이방식] :
- 문자열을 하나씩 모두 확인하여 계산 로직 확인하는 방법, eval함수 활용.
    - 입력문자열을 deque()로 바꿔서 왼쪽부터 각 문자(ch)를 숫자 or 문자 판별하기
    - 1. ch가 숫자의 경우, 임의의 변수 tmp에 저장해두기(2자리수 정수를 염두해둔 부분) >> tmp가 빈 값이 아닐 때, result에 리스트 요소로 저장
    - 2-1. ch가 문자고 S,D,T인 경우, result의 마지막 값에 제곱근 문자열 추가 저장하기
    - 2-2. ch가 *,#인 경우 처리하기
    - 3. result의 문자열 요소들을 '+'로 이어붙인 후, eval함수 사용하여 계산.

'''

from collections import deque
def solution(dartResult):    
    # 그리디?
    # eval함수 사용하기
    
    q = deque(dartResult)
    result = []
    tmp = ''
    
    while q :
        ch = q.popleft()
        
        #1. 숫자 확인
        if ch.isdigit():
            tmp +=ch
            continue
        elif tmp !='' :             # tmp가 빈 값이 아닌 경우(+ch는 숫자가 아닌 상황), 이전 ch의 값을 result에 저장. >> 두 자릿수
            result +=tmp,
            tmp=''

        #2-1. 문자 확인, 보너스
        if ch.isalpha() and ch == 'D':
            result[-1]+='**2'
        elif ch.isalpha() and ch == 'T':
            result[-1]+='**3'
        # ch =='S' pass
        
        #2-2. 문자 확인, 옵션
        if ch =='*':
            result[-1]+='*2'
            if len(result)>=2:          # 이전 값까지 곱하기
                result[-2]+='*2'

        elif ch =='#':
            result[-1]+='*(-1)'
            
    
    result = '+'.join(result)
    return eval(result)

# other solution
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')           # (\d+) : 숫자 매치, 최소 1번 이상 숫자
                                                    # ([SDT]) : [해당문자]에 해당 되는 것
                                                    # ([*#]?) : [해당문자]? 있어도 없어도 됨 의미 
    dart = p.findall(dartResult)                # dart[0]은 무조건 (숫자,SDT,*#?)으로 구성됨.
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:         # dart[i][2] >> ()()(여기에 해당됨)
            dart[i-1] *= 2                      # 이전값에 2배곱 계산
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] # 해당 위치를 계산 결과값으로 재설정

    answer = sum(dart)
    return answer