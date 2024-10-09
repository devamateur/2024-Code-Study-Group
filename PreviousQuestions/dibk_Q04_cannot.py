'''
🍪문제 번호 :
11장 그리디 - 04 : 만들 수 없는 금액

🍈문제 정의 :
N개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값을 구하기.

🍊풀이 시간 :
10분

🍒풀이 방법 :

'''
class Solution :

    def run(self):
        # 입력
        n = int(input())
        coins = list(map(int,input().split()))
        coins.sort()
        
        amount = 1
        for n in coins :
            if amount < n :
                break
            amount +=n
        
        print("결과 : ",amount)
        return 
    
test = Solution()
test.run()