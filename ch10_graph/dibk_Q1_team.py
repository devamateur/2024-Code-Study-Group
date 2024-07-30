'''
🍪문제 번호 :
10장 실전문제 - 팀 결성

🍈문제 정의 :
학생들에게 0~N번까지의 번호를 부여했다. 모든 학생이 서로 다른 팀으로 구분되어 N+1개의 팀이 존재한다.   
'팀 합치기'(0),'같은 팀 여부 확인'(1) 연산을 사용할 수 있는데, M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하기   
입력값 : N(부여번호 갯수),M(연산 갯수)   
출력값 : 같은 팀 여부 확인' 연산에 대한 결과(yes, no)   

🍊풀이 시간 :
12분

🍒풀이 방법 :
우선,  0~N번 딕셔너리 생성하고(양방향, 각 번호key가 속해있는 팀원value을 저장)   
'팀 합치기'(0)이 입력되면 위 딕셔너리를 갱신, 같은 팀 여부 확인'(1)이 입력되면 딕셔너리 조회

'''

class Solution :
    
    def teamFormation(self):
        # 입력
        N, M = map(int,input("노드 갯수N, 연산의 갯수M : ").split())
        
        graph = {}
        answer = []

        for _ in range(M):
            op, n1,n2 = map(int,input().split())
            
            if op == 0:
                graph[n1] = graph.get(n1,[]) + [n2]
                graph[n2] = graph.get(n2,[]) + [n1]     # 양방향
            
            elif op == 1 :
                if n1 not in graph or n2 not in graph[n1] :
                    answer +='NO',
                else :
                    answer +='YES',
        
        for result in answer :
            print(result)
        
        return 
    
test = Solution()
test.teamFormation()