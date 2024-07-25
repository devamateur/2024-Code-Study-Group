'''
🍪문제 번호 :
8장 실전문제 - 효율적인 화폐 구성

🍈문제 정의 :
N가지 종류의 화폐를 최소로 이용하여 가치합이 M원이 되도록 구하기(경우의 수:조합)
M원을 만드는 최소 화폐 갯수 구하기

🍊풀이 시간 :
10분(failed : 문제 예시만 해결)
failed ex) N=3, K=7, [2,3,5] 

🍒풀이 방법 :
failed)화폐의 단위를 큰수 순으로 정렬하여 나머지가 0인 경우에 결과를 도출하는 단순 그리디 알고리즘.
solution)
- 화폐 단위 갯수 N, 전체 M
- 화폐단위(coin)를 기준으로 전체값 for문을 순회한다 : O(N) * O(M-N)
    - 현재위치-coin : 현재위치에서 화폐단위(coin)를 뺀 화폐의 구성값을 가져와야한다.
    - coin:3, 현재위치:4 > 현재위치(4)를 구성할때, coin(3)을 제외하고 1단위 화폐가 존재한다면, 1단위의 값+1// 없다면 pass

'''

class Solution :
    
    def moneyComposition(self):
        # 입력
        N, M = map(int,input("종류(N), M원 입력: ").split())
        currency = []
        for _ in range(N):
            currency += int(input()),
        
        dp = [10001]*(M+1)      # M공간에 최대값10001로 정의
        dp[0]=0
        
        for coin in sorted(currency):
            # 화폐단위부터 for문 시작 : 2,3,5
            for p in range(coin,M+1):           
                if dp[p-coin]!=10001 :      # 현재위치-화폐단위 : 현재위치값을 구하려면 화폐단위를 제외한 화폐가 필요한데 해당 값이 있다면
                    dp[p] = min(dp[p],dp[p-coin]+1)
        
        answer = -1 if dp[M] == 10001 else dp[M]
        print("결과 : ",answer)
        return 
    
    
    # failed
    def composition(self):
        # 입력
        N, M = map(int,input("종류(N), M원 입력: ").split())
        coin = []
        for _ in range(N):
            coin += int(input()),
        
        answer = 0
        for c in sorted(coin,reverse =True):
            if M%c == 0 :
                answer = M //c
                break
        answer = answer if answer else -1
        print("결과 : ",answer)
        return 
    
test = Solution()
test.moneyComposition()