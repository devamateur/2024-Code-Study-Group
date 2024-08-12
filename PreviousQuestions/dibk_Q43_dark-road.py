'''
🍪문제 번호 :
18장 그래프 이론 - 43번 어두운 길

🍈문제 정의 :
N개의 집은 0~N-1번까지의 번호로 구분되어 있고, M개의 도로는 가로등이 구비되어 있다.
특정 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다

🍊풀이 시간 :
30분

🍒풀이 방법 :
- 크루스칼 알고리즘 문제에 해당됨 : 일부 가로등을 비활성화, 최대한 많은 금액 절약
- 가로등이 모두 활성화된 비용 - 일부 활성화된 비용 값을 구해야 함.
'''

class Solution :
    
    def gate(self):
        # 함수
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union_(a, b):
            a = find(a)
            b = find(b)

            if a < b:
                parent[b] = a
            else :
                parent[a] = b
        
        # 입력
        N, M = map(int,input("집의 수N, 도로의 수M : ").split())
        parent = [i for i in range(N+1)]

        edges = []
        for _ in range(M) :
            # x,y 사이의 양방향 도로, 비용(길이)은 z
            x,y,z = map(int,input().split())
            edges += [z,x,y],            # 비용 기준
        
        edges.sort()                    # 비용 기준
        
        result = 0
        total = 0
        for edge in edges :
            cost, a, b = edge
            total+=cost
        
            if find(a) != find(b) :
                union_(a,b)
                result +=cost       
        
        print("결과 : ",total-result)
        return 
    
test = Solution()
test.gate()