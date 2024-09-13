'''
🍪문제 번호 :
13장 DFS/BFS - 18 : 괄호 변환
https://school.programmers.co.kr/learn/courses/30/lessons/60058

🍈문제 정의 :
'균형잡힌 괄호 문자열'이 매개변수로 입력될 때, "올바른 괄호 문자열"로 변환하여 출력하기

🍊풀이 시간 :


🍒풀이 방법 :


'''

# solution
# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


# failed 
def solution(p):
    if not p : return p
    
    answer = ''
    
    def check_true():
        left,right = 0,len(p)-1
        
        while left!=right:
            if p[left]!=p[right]:
                left +=1
                right -=1
                continue
            
            if p[right] == "(":
                right +=1
                continue
            ...
        
        return
    
    def division(text):
        left,right = 0,0
        
        return u,v

    
    return answer
