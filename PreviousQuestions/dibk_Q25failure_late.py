'''
🍪문제 번호 :
14장 정렬 - 25 : 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889

🍈문제 정의 :
input - 전체 스테이지 수(N), 게임 이용자가 멈춰있는 스테이지 번호 배열 stage
output - 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨 있는 배열을 return

🍊풀이 시간 :
20분 but failed
채점 결과
정확성: 70.4
합계: 70.4 / 100.0

🍒풀이 방법 :
진짜 단순하게 생각해서 문제풀이
1)stages(유저들이 멈춘 스테이지 번호들)을 정렬하기   -  해당 스테이지에서 유저들을 지우기 위해 활용
2) for문을 돌면서 stages의 수, 실패한 사람 수, 실패율, stages에서 못 넘은 유저들 삭제 처리 과정을 진행함.
3) answer에는 실패율과 스테이지 번호를 기록함.

filter함수 시간복잗도, 인덱싱 시간복잡도 때문에 런타임 에러 발생한 것으로 추측됨.

솔루션을 참고해서 살펴보니, count함수를 썼다면 아주 이지했겠구낳ㅎㅎㅎㅎㅎㅎ

'''
def solution(N, stages):
    answer = []
    stages.sort()

    for i in range(N):
        lv = i+1
        numbers = len(stages)
        failed = len(list(filter(lambda x : x<=lv,stages)))
        late = failed/numbers
        answer += (late,lv),
        
        stages = stages[failed:]
        
    answer.sort(key=lambda x : (-x[0],x[1]))

    return [b for a,b in answer]

##

def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer