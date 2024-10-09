'''
🍪문제 번호 :
11장 그리디 - 1번 모험가 길드

🍈문제 정의 :
모험가 N명을 대상으로 공포도를 측정했는데, 공포도가 높은 모험가는 쉽게 공포를 느껴 위험상황을 제대로 대체할 능력이 부족함.
모험가 그룹을 안전하게 구상하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음.
최대 몇 개의 모험가 그룹을 만들 수 있는지 구하기.

🍊풀이 시간 :
25분

🍒풀이 방법 :
딕셔너리를 만들고(key(공포값) : value(빈도))
value값이 높은 순으로 체크하기

solution과 비슷함. 해당 풀이는 직관적이지 않음.

'''
class Solution :
    
    def guild(self):
            
        # 입력
        N = int(input("모험가 수 : "))
        fear_level = list(map(int,input().split()))
        
        # O(N)
        fear_dict = {}
        for c in fear_level :
            fear_dict[c] = fear_dict.get(c,0) +1
        
        # O(N) + NlogN
        tmp = list()
        for k,v in sorted(fear_dict.items(),key=lambda x : (x[1],x[0])):
            tmp.extend([k]*v)
        
        # O(N)
        team = 0            # 현재 한 팀의 인원수
        result = 0          # 총 그룹 수
        while tmp :
            person = tmp.pop()
            
            if team < person :
                team +=1
            else :
                result +=1
                team = 1

        print("결과 : ",result)
        return 
    
    def real_solution(self):
        n = int(input())
        data = list(map(int, input().split()))
        data.sort()

        result = 0 # 총 그룹의 수
        count = 0 # 현재 그룹에 포함된 모험가의 수

        for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
            count += 1 # 현재 그룹에 해당 모험가를 포함시키기
            if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
                print(count,i)
                result += 1 # 총 그룹의 수 증가시키기
                count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

        print(result) # 총 그룹의 수 출력
    
test = Solution()
test.guild()