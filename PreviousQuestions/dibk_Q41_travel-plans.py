'''
🍪문제 번호 :
18장 그래프 이론 - 41번 여행 계획

🍈문제 정의 :
N개의 여행지는 서로 연결하는 도로가 존재하며 양방향성을 띄고 있다. 한울이는 하나의 여행 계획을 세운 뒤에 해당 계획이 가능한지 여부를 판단하고자 한다.

🍊풀이 시간 :
30분

🍒풀이 방법 :
- 양방향 그래프 문제이므로 크루스칼, 위상 정렬 알고리즘X
- 서로 연결되어 있는 것을 서로소 집합 알고리즘으로 확인(부모노드가 다르면 연결X 의미)
'''

class Solution :
    
    def travel_plans(self):
        # 함수
        def find_parent(parent,x):
            if parent[x] != x:
                parent[x] = find_parent(parent,parent[x])
            return parent[x]
        
        def union_parent(parent,a,b):
            a = find_parent(parent,a)
            b = find_parent(parent,b)
            
            if a < b :
                parent[b] = a
            else :
                parent[a] = b
            
        # 입력
        N, M = map(int,input("여행지의 수N, 도시의 수M : ").split())
        
        parent = [0]*(N+1)      
        for i in range(1,N+1):
            parent[i] = i
        
        for row in range(N):
            tmp = map(int,input().split())
            
            for col,value in enumerate(tmp) :
                if value == 0 : continue
                union_parent(parent,row+1,col+1)
        
        print(parent)
        # run
        plan = list(map(int,input("여행 계획 : ").split()))
        
        print()
        print()
        
        for i in range(1,len(plan)) :
            if find_parent(parent,plan[i-1]) != find_parent(parent,plan[i]) :
                print("결과 : NO")
                break
        else :
            print("결과 : YES")
        
        return 
    
test = Solution()
test.travel_plans()