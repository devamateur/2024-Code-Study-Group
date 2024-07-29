'''
🍪문제 번호 :
9장 실전문제 - 전보

🍈문제 정의 :
N개의 도시가 있으며 단방향의 통로가 존재한다. N(도시갯수), M(통로갯수),C(출발도시)를 입력하여 최대한 많은 도시를 순회하면 얼마나 걸리는 지 구하기.
출력값은 방문한 모든 도시 갯수와 걸린 시간

🍊풀이 시간 :
20분

🍒풀이 방법 :
DFS방법으로 모든 경로에서 방문한 도시가 많은 경로를 탑다운으로 저장하여 최댓값 구하기(방문 도시 갯수 기준 max)
이전문제인 '미래 도시'와 비슷한 풀이.

'''

class Solution :
    
    def throughoutTheCity(self):
        # 입력
        N, M, C = map(int,input("도시 갯수N, 경로의 개수M, 시작도시 : ").split())
        
        graph = {}
        
        for _ in range(M):
            n1,n2,time = map(int,input().split())
            graph[n1] = graph.get(n1,[]) + [(n2,time)]
 
        def recursive(start):
            if start not in graph : return 1,0
            
            cities,time = 0,0
            for (arrival,m_time) in graph[start]:
                stopby,_ = recursive(arrival)
                if cities < stopby :            # 이전 depth의 stopby가 카운팅이 많다면,
                    time +=m_time+_             # time과 cities를 max값 기준으로 재설정
                    cities = stopby+1
            return cities,time

        answer_count,answer_time = recursive(C)
        print("결과 : ",answer_count,answer_time)
        return 
    
test = Solution()
test.throughoutTheCity()