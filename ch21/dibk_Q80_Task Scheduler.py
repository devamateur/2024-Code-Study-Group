'''
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/description/

[time] 4h
[문제] A~Z로 표기된 TASK는 쿨링시간이 n이다. 순서에 상관없이 task를 완료할 수 있는데, 같은 TASK들은 적어도 n간격 텀으로 실행된다. 최소 실행을 출력.
[풀이방식] :
- 야매
- 


'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task의 빈도 구하기
        task_dict = {}
        for ch in tasks:
            task_dict[ch] = task_dict.get(ch,0)+1

        tmp = []            # 임시로 저장하는 리스트
        p = 0               # tmp내에서 움직이는 포인터
        saved = deque()     # 임시저장 리스트(tmp전용)

        while task_dict or saved :  # task_dict, saved가 둘 다 0이되면 break
            
            if p>=len(tmp):                         # 포인터p가 tmp길이를 벗어나면,
                while saved :                       # saved에 저장해둔 dictionary값을 복원
                    comp= saved.popleft()
                    if comp[1] != 0:                # value가 0이면 패스
                        task_dict[comp[0]] = comp[1]

                if not task_dict :                  # 더이상 task_dict가 없으면(while saved 했을 때, 아무것도 없다면) while문 빠져나가기.
                    break
                
                ch = max(task_dict,key = task_dict.get)     # ch에 가장 큰 값의 key문자를 입력
                tmp += [ch] + ['0']*n                       # tmp에 더하기 ex) AB0'A00'
                saved = deque([[ch,task_dict[ch]-1]])       # saved에 해당 문자 딕셔너리를 임시로 넣어두기
                task_dict.pop(ch)                           # task딕셔너리에는 임시로 빼두기

            else :
                if task_dict :                              # task_dict에 값이 있으면 ch를 갱신해서 작업, but 없으면 pointer만 이동하게 됨(p+=1)
                    ch = max(task_dict,key = task_dict.get)
                    tmp[p]=ch

                    saved.append([ch,task_dict[ch]-1])
                    task_dict.pop(ch)
                
            p+=1

  
        while tmp :                             # 끝값이 0인경우 지우기
            if tmp[-1] == '0' :
                tmp.pop()
            else :
                return len(tmp)

