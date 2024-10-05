def solution(n, build_frame):
    answer = []
    # answer: x, y(기둥, 보의 교차점 좌표), a(기둥 or 보)
    # build_frame: x, y, a: 기둥 or 보(0/1), b: 삭제 or 설치(0/1)
    
    def make_pillar(x, y):
        # 기둥: 바닥 위 or 보의 한쪽 끝 위 or 다른 기둥 위
        if y == 0 or [x, y, 1] in answer or  [x-1, y, 1] in answer or [x, y-1, 0] in answer:
            return True
        return False
        
    def make_beam(x, y):
        # 보: 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 연결
        if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
            return True
        return False
        
    
    for x, y, a, b in build_frame:
        # 삽입
        if b == 1:
            if a == 0:        # 기둥
                if make_pillar(x, y):
                    answer.append([x, y, a])

            else:
                if make_beam(x, y):
                    answer.append([x, y, a])

        # 삭제
        else:
            answer.remove([x, y, a])    # 해당 요소를 일단 삭제

            # 삭제하고 난 뒤 구조물의 상태 확인
            for ax, ay, aa in answer:
                # 삭제한 뒤 기둥이나 보가 조건을 만족하지 않으면 삭제한 요소를 다시 설치
                if aa == 0 and not make_pillar(ax, ay):
                    answer.append([x, y, a])
                elif aa == 1 and not make_beam(ax, ay):
                    answer.append([x, y, a])
                        
    answer.sort()    # 구조물을 좌표순 정렬
    
    return answer