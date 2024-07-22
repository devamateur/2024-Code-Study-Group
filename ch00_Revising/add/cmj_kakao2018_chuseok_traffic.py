import datetime

'''
초당 최대 처리량: 임의 시간부터 1초(1000밀리초)간 처리하는 요청의 최대 개수 (응답 완료 여부 상관x)

lines: 날짜 S T 형태
ex) 2016-09-15 03:10:33.020 0.011s
- S: 응답완료시간 = 종료시간
- T: 처리시간 (시각시간과 끝시간을 포함)

=> 시작시간 = S - T + 0.001

lines 배열에 대해 초당 최대 처리량 리턴하기

'''

# 1. datetime을 이용하는 방법(답 풀이)
def solution1(lines: str) -> int:
    # 로그의 시작, 종료 시각 저장
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        
        # datetime.strptime(): 날짜 형식 데이터를 datetime 형식으로 바꿈
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        #print(timestamp)
        
        # timestamp를 이용해 시작시간, 종료시간을 튜플 형태로 넣어줌
        combined_logs.append((timestamp, -1))      # 종료시간
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))             # 시작시간 = timestamp - 처리시간(T)+0.001
        
    accumulated = 0
    max_requests = 1
    
    # 로그를 시간순으로 오름차순 정렬
    combined_logs.sort(key=lambda x: x[0])

    for i, elem1 in enumerate(combined_logs):
        current = accumulated
        
        # 1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            # 두 로그의 차이가 0.999보다 크면 break
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:        # elem2가 시작시간인 경우
                current += elem2[1] # 카운트 증가
        max_requests = max(max_requests, current)
        accumulated += elem1[1]

    return max_requests

# 2. 직접 시간 변환
def solution2(lines: str) -> int:
    # 로그의 시작, 종료 시간을 저장하는 리스트
    S , E= [], [] 

    for line in lines:
        (d,s,t) = line.split(" ")   # 로그 날짜, 종료 시간, 처리 시간

        # 초 변환
        t = float(t[:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)           # 종료 시간, 이전 작업의 종료-다음 작업의 시작 시간이 1초에 해당하는 경우를 카운트하기 위해 +1
        S.append(seconds - t + 0.001)   # 시작 시간

    # 로그 시작 시간 정렬
    # 종료 시간은 이미 정렬된 상태로 주어졌으므로 정렬X
    S.sort()

    # 각 시간대의 트래픽을 계산함
    cur_traffic = 0
    max_traffic = 0
    i = j = 0
    
    while((i < len(lines)) & (j < len(lines))):
        if(S[i] < E[j]):       # 현재 종료 지점보다 작은 시작 지점 카운트 (종료 지점 안에 있는 시작 지점 카운트)
            cur_traffic += 1
            max_traffic = max(max_traffic, cur_traffic)
            i += 1
        else:                ## 더이상 현재 종료 지점 안에 있는 시작 지점이 없으면, 다음 종료 지점으로 넘어감
            cur_traffic -= 1
            j += 1

    return max_traffic