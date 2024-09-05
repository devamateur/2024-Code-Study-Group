import collections
def solution(N, stages):
    answer = []
    
    # 실패율 = 스테이지에 도달했지만 클리어못한 플레이어 수 / 스테이지에 도달한 전체 플레이어 수
    stages.sort()
    
    for i in range(1, N+1):
        current_player = stages.count(i)              # 스테이지에 도달했지만 클리어못한 플레이어
        total_player = 0
        
        if current_player == 0:        # 분자가 0이면 실패율 0
            fail_rate = 0

        # 스테이지에 도달한 전체 플레이어 수 = 현재 스테이지보다 크거나 같은 스테이지 수
        # ex) 현재 스테이지2이면 2보다 크거나 같은 스테이지 수
        for j in range(len(stages)):
            if stages[j] >= i:
                total_player += 1
            
        if total_player == 0:          # 분모 0이면 실패율 0
            fail_rate = 0
        else:
            fail_rate = current_player / total_player

        # 스테이지, 스테이지 실패율 저장    
        answer.append((i, fail_rate))
    
    # 스테이지 실패율 기준 내림차순
    answer.sort(key=lambda x:x[1], reverse=True)
    
    return [a[0] for a in answer]         # 스테이지만 리턴