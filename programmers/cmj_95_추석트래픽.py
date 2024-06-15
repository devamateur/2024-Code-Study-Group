import datetime

def solution(lines: str) -> int:
    # 로그의 시작, 종료 시각 저장
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        
        # datetime.strptime(): 날짜 형식 데이터를 datetime 형식으로 바꿈
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))      # 종료시간
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))       # 시작시간 = timestamp - 처리시간(T)+0.001
        
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
            if elem2[1] > 0:      # 시작 시간이면 1 증가
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]

    return max_requests