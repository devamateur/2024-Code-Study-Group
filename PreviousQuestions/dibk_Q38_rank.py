'''
🍪문제 번호 :
17장 최단경로 - 38번 정확한 순위

🍈문제 정의 :
일부 학생 성적 데이터만으로 학생들의 성적 순위를 계산하여 정확한 순위를 알 수 있는 학생의 수를 구하기

🍊풀이 시간 :


🍒풀이 방법 :
- 최단경로 문제로 인식되지 않음, 위상정렬(그래프) 문제로 느껴짐
    - https://velog.io/@embeddedjune/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC-Q38-%EC%A0%95%ED%99%95%ED%95%9C-%EC%88%9C%EC%9C%84
    - A,B학생 사이의 성적을 비교할 때 A와 B사이에 경로가(다른 학생이) 존재한다면, 거처가는 정점을 기준으로 수행해야함 >> 플로이드 알고리즘 문제
    
- 플로이드 알고리즘은 A,B 사이에 직항과 경유 비용을 비교하여 짧은 값을 찾는 것.

문제 핵심 : 
- if graph[i][j] == graph[j][i] == INF :: 다른 학생이 자기보다 성적이 낮거나 높은지 알 수 없는 경우에는, 순위는 알 수 없다

 자기보다 성적이 높은 학생에게 도달 가능하고(그래서 성적이 높은 학생 수를 알 수 있고),
 자기보다 성적이 낮은 학생이 자기에게 도달 가능하면(그래서 성적이 낮은 학생 수를 알 수 있으면) 정확한 순위를 알 수 있다.
 즉, 자기보다 성적이 낮은 학생 수 + 자기보다 성적이 높은 학생 수 = 총 학생 수 이어야 한다.
https://velog.io/@juyeonma9/%EC%9D%B4%EC%BD%94%ED%85%8C-%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C-%EC%A0%95%ED%99%95%ED%95%9C%EC%88%9C%EC%9C%84-python

'''
class Solution :
    
    def rank(self):
            
        # 입력
        N,M = map(int,input("학생 수, 비교한 횟수 : ").split())
        INF = int(1e9)
        info = [[INF]*(N+1) for _ in range(N+1)]
        
        for i in range(1,N+1):
            for j in range(1,N+1):
                info[i][j] = 0          # 초기화
        
        for _ in range(M) :
            a,b = map(int,input().split())
            info[a][b] = 1
            
        for k in range(1, N + 1):
            for a in range(1, N + 1):
                for b in range(1, N + 1):
                    info[a][b] = min(info[a][b], info[a][k] + info[k][b])
        
        result = 0
        # 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
        for i in range(1,  N + 1):
            count = 0
            for j in range(1, N + 1):
                if info[i][j] != INF or info[j][i] != INF:              # 해당 i,j 학생 끼리의 경로가 있다면(무한 값이 아닌 값이 존재한다면)
                    count += 1
            # count가 전체 학생수와 같다면??? :: 해당 위치에서(i) 위아래 순위를 확인할 수 있다(경로가 있다)는 의미임으로 i의 순위, 위치를 알 수 있다는 뜻
            if count == N:
                result += 1
    
test = Solution()
test.rank()