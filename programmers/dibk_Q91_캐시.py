'''
캐시
https://school.programmers.co.kr/learn/courses/30/lessons/17680

[time] 15m
[풀이방식] :
*LRU(Least Recently Used) : 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법(https://j2wooooo.tistory.com/121)(https://velog.io/@ddyy094/LRULeast-Recently-Used-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EB%9E%80)
*Cache Hit : CPU 가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우
*Cache Miss : CPU 가 참조하고자 하는 메모리가 캐시에 존재하지 않을 경우

- cities를 순회하며 nodes에 도시를 입력 및 삭제를 통해 캐시 교체 실행 시간을 계산한다.
- city가 nodes의 중간 위치에 존재하면, remove로 삭제 후, 맨 뒤에 다시 입력하여 city의 저장 위치를 바꾼다.
- nodes 크기가 초과하면 자동으로 왼쪽(가장 먼저 입력된 도시)가 삭제된다.(deque(maxlen=cacheSize))

'''

# 테스트 케이스 통과, 제출 시간초과 >>> 수정 후 완성
from collections import deque
def solution(cacheSize, cities):
    nodes = deque()                 # 수정 : deque(maxlen=cacheSize)
    answer=0                        # maxlen 이상의 값을 추가할 경우, append()을 하게 되면 맨 왼쪽의 원소가 삭제
    
    for city in cities :
        city = city.upper()
        
        if city in nodes :
            nodes.remove(city)
            answer+=1
            nodes.append(city)
            continue
        
        if len(nodes) > cacheSize:      # 수정 : 삭제
            nodes.popleft()
            
        nodes.append(city)
        answer+=5
    
    return answer
