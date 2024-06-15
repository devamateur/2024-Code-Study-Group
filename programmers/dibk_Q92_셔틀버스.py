'''
셔틀버스
https://school.programmers.co.kr/learn/courses/30/lessons/17678

[time] failed
[풀이방식] :
- 크루들의 시간을 분 단위로 전처리 및 정렬 후, n회 버스 운행, m명 타임확인을 통해 마지막 m명째의 시간보다 1분 전 시간을 정답(candidate)로 저장한다.
    - m명째 크루의 시간이 9시보다 작은 경우(crews[0]<=current), 그 크루의 시간에 1분전의 값을 저장해두기(crews.popleft() - 1) :: 이 부분이 문제풀이 핵심

'''

# solution
from collections import deque
def solution(n, t, m, timetable):
    # 크루들의 시간을 분 단위로 변환
    timetable.sort()
    crews = deque()
    for time in timetable :
        hh,mm = time.split(':')
        total = int(hh)*60 + int(mm)
        crews.append(total)

    current = 540                   # 오전 9시부터 시작
    for _ in range(n):              # 버스 운행 횟수
        for _ in range(m):
            # 대기가 있는 경우 1분 전 도착
            if crews and crews[0] <= current:            
                candidate = crews.popleft() - 1
            else:  # 대기가 없는 경우 정시 도착
                candidate = current

        current += t
    # 시, 분으로 다시 변경
    h, m = candidate//60, candidate%60
    return str(h).zfill(2) + ':' + str(m).zfill(2)


## failed
def solution(n, t, m, timetable):
    # 버스 시간표
    bus = {}
    hh,mm = 9,0
    for _ in range(n) :
        bus[(hh,mm)] = 0
        mm+=t
        hh += mm//60
        mm = mm%60
    
    # crews
    timetable.sort()
    for crew in timetable :
        hh,mm =crew.split(':')
        print(hh)
        # 여기서 막힘..
        