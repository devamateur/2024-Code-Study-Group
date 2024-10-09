'''
🍪문제 번호 :
11장 그리디 - 06 : 무지의 먹방 라이브
https://school.programmers.co.kr/learn/courses/30/lessons/42891

🍈문제 정의 :
링크 참조

🍊풀이 시간 :
10분 but failed(반틀리고 반 맞고)

🍒풀이 방법 :
solution에서는 큐를 쓰는데 왜 큐르 쓰지????
문제 자체를 이해 못한 것 같음

'''

def solution(food_times, k):
    # 음식 번호 인덱스 포인터
    idx = 0
    size = len(food_times)
    
    while k :
        if sum(food_times) <= k:
            return -1
        
        for _ in range(size) :
            if food_times[idx] :
                break 
            idx = (idx+1)%size

        else :
            # while문 out
            k = 0
            break
            
        food_times[idx] -=1
        idx = (idx+1)%size
        k -=1
        
    return idx+1

import heapq

# soltion
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]