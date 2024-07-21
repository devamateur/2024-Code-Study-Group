'''
🍪문제 번호 :
2018 카카오 블라이드 테스트 - 1차 추석 트래픽
https://school.programmers.co.kr/learn/courses/30/lessons/17676

🍈문제 정의 :   
하루의 초당 최대 처리량을 구하는 문제로, **1초(1000ms)에 최대로 처리되고 있는 작업 갯수**를 구하기.
- (list)lines :: 문자열로 구성되었으며 "2016-09-15 hh:mm:ss.sss" 형식으로 고정됨.
- (str) T :: 0.1s, 0.312s 같이 뒤에는 초단위를 의미하는 s로 끝난다.
- 처리시간은 0.001 ≦ T ≦ 3.000

ex) 2016-09-15 03:10:33.020 0.011s   
9월 15일 오전 3시 10분 33.020초까지 0.011초 동안 처리된 요청

🍊풀이 시간 :
failed

🍒풀이 방법 :
1) 작업의 시작시간과 끝시간을 저장한다.(start,end)
    - 작업의 시작은 시간,분,초를 초단위로 단위를 맞춰서 저장해둠.
    - 끝 시간에는 +1초를 더한다. >>> 2)에서 설명

2) 시작시간 리스트와 끝시간 리스트를 비교하며 처리 작업 갯수를 확인함
- start의 작업들이 end의 작업보다 값이 작으면 current에 +1하여 처리 작업 갯수를 추가함
- 현재의 start 작업 시간이 end 시간보다 크다면 current를 -1하고, start 작업시간이이 end보다 작아질때까지 처리작업(current) 갯수는 작아진다.
    - 1)에서 끝작업시간에 1초를 더했는데 :: 원래작업끝 + 1초 사이에 새로운 시작작업시간이 있다면 그 1초 사이에 작업갯수를 세어야 하기 때문
    - window사이즈는 무조건 1초(1000ms)로 고정되어 있기 때문에, 연속적으로 작업이 진행되지 않아도 그저 1초 사이에 시작과 끝이 있다면 카운팅을 해야함.

'''
# solution
def solution(lines):
    start,end = [],[]
    for line in lines :
        date,time,t = line.split(" ")                               # 어챂피 date는 의미 없음
        task = float(t[:-1])
        hh,mm,ss = time.split(":")
        
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)     # float으로 변환해주므로 초의 뒤단위를 살림.
        
        start.append(seconds-task+0.001)                            # 작업의 시작은 time에서 task를 빼고 0.001을 시작으로 함.
        end.append(seconds+1)                                       # 작업끝나고 +1초 사이까지의 작업수를 확인하기 위해서.
    
    start.sort()                                                    # lines는 오름차순으로 정렬되있어서 end는 정렬하지 않아도 됨.
    totaltask = len(lines)
    
    current = 0                                                     # 1초 안에 작업하고 있는 테스크의 갯수
    max_ = 0
    s_idx,e_idx = 0,0                                               # start와 end의 인덱스 
    
    while (s_idx<totaltask)&(e_idx<totaltask):
        if start[s_idx] < end[e_idx] :
            current +=1
            max_ = max(max_,current)
            s_idx +=1
        
        else :
            # start의 작업 시작이 end보다 높으면 
            current -=1
            e_idx +=1
    
    return max_
