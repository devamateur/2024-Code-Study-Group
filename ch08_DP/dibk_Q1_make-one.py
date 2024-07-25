'''
🍪문제 번호 :
8장 실전문제 - 1로 만들기

🍈문제 정의 :
입력값인 정수X가 주어질 때, 4가지 오퍼레이션을 활용하여 1을 만들려고 한다. 최소 연산 횟수를 구하기
*3장 그리디의 '1이 될때까지' 문제와 유사

🍊풀이 시간 :
40분

🍒풀이 방법 :
- 4가지 연산을 순서대로 진행하여 최소 연산 횟수를 구하려고 했는데 2나눗셈 때문에 풀이방법을 다시 생각해야 했다.(그리디)
- DFS방식(탑다운)으로 1이 되는 모든 연산과정을 실행함. 실행횟수가 적은 것을 리턴하기.
    - 입력값은 -1 연산으로 모두 통과가 가능하다.(==false가 없다)(ex)입력값 26에 대해 최대 26회 실행, 연산 실패가 없다.
    - recursive함수는 매개변수는 정수, 리턴값은 연산횟수이다.
    - recursive의 끝은 입력값이 1이될 때 0을 리턴하여, 상위단계에서 count와 비교하여 리턴 단계의 최소위치를 count에 담아두도록 한다.
'''

class Solution :
    
    def makeOne(self):
        # 입력
        X = int(input("정수 입력 : "))

        def recursive(num):
            if num == 1: return 0           # 마지막 depth 의미

            count = 10000
            for op in [5,3,2]:
                if num%op==0 :
                    bool_ = recursive(num//op)
                    count = min(bool_,count)
            else :
                num -=1
                bool_ = recursive(num)
                count = min(bool_,count)            # for[5,3,2]에서 recursive()를 수행한 bool_값이 작으면 count는 작은 값을 기록하므로 문제 없다.
                return count+1                      # 다음 depth로 이동
        
        answer = recursive(X)
        print("결과 : ",answer)
                                                 
        
        return 
test = Solution()
test.makeOne()