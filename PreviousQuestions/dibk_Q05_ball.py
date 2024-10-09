'''
🍪문제 번호 :
11장 그리디 - 05 : 볼링공 고르기

🍈문제 정의 :
N개의 볼링공이 있으며 각 자 무게가 다름. 문제 작성하기 너무 귀찮다.

🍊풀이 시간 :
5분

🍒풀이 방법 :
문제가 너무 단순한걸

'''
class Solution :

    def run(self):
        # 입력
        n,m = map(int,input().split())
        ball = list(map(int,input().split()))
        
        result = 0
        for i in range(n):
            for j in range(i+1,n):
                if ball[i] !=ball[j]:
                    result +=1
        
        print("결과 : ",result)
        return 
    
test = Solution()
test.run()