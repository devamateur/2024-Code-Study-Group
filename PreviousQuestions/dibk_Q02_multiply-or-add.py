'''
🍪문제 번호 :
11장 그리디 - 02 : 곱하기 혹은 더하기

🍈문제 정의 :
0-9로 이뤄진 문자열S가 주어졌을 때, 왼오른쪽으로 하나씩 숫자를 확인하며 숫자 사이에 곱/더하기 연산을 넣어 만들 수 있는 큰 수를 구하기

🍊풀이 시간 :
10분

🍒풀이 방법 :
easy~

'''
class Solution :
    def operation(self,a,b):
        if a+b > a*b :
            return a+b
        return a*b
    
    def run(self):
            
        # 입력
        S = str(input())
        result = int(S[0])
        
        for i in range(1, len(S)):
            output = self.operation(result,int(S[i]))
            result = output
        
        print("결과 : ",result)
        return 
    
test = Solution()
test.run()