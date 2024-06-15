'''
뉴스 클러스터링
https://school.programmers.co.kr/learn/courses/30/lessons/17677

[time] 30m
[풀이방식] :
*J(A,B) = P(A∩B)/P(AUB)
- 각 문자열을 두 글자씩 끊어서 다중집합 만들고, 그 집합의 빈도 딕셔너리 생성
- adict 순회시, 중복요소는 min값을 교집합 수에 더하고, bdict 순회시, 중복요소의 max값을 합집합 수에 더하여 answer 구하기

'''

from collections import Counter
def solution(str1, str2):
    
    #1. 문자열을 2크기로 잘라서 다중집합 만들기
    a = []
    b = []
    
    for i in range(1,len(str1)):
        if str1[i-1:i+1].isalpha():
            a += str1[i-1:i+1].upper(),
    
    for i in range(1,len(str2)):
        if str2[i-1:i+1].isalpha():
            b += str2[i-1:i+1].upper(),
    
    #2. 위에서 만든 집합의 빈도사전 만들기
    adict = {}
    for ch in a:
        if not ch in adict :
            adict[ch]=0
        adict[ch]+=1
    
    bdict = {}
    for ch in b:
        if not ch in bdict :
            bdict[ch]=0
        bdict[ch]+=1
    
    #3. 각 딕셔너리를 활용하여 교집합, 합집합 수 구하기
    inters = 0
    union = 0
    for k,v in adict.items():
        if k in bdict :
            tmp = min(v,bdict[k])
            inters +=tmp                # 교집합에서는 두 딕셔너리 빈도의 min값 더하기
            continue                    # adict에서는 합집합(union) 수를 계산하지 않고 bdict에서 계산하기(이중더하기 방지)
        union +=v
        
    for k,v in bdict.items():
        if k in adict :
            v = max(v,adict[k])        # 교집합에서 두 빈도의 max값을 구하고
        union +=v                      # 합집합에 값을 더하기. 위에서 교집합 시, union수를 계산하지 않았기 때문에 여기서 값을 더해줘야함.
    
    answer = 1 if union ==0 else inters/union
    return int(answer*65536)
            