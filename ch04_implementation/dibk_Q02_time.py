'''
🍪문제 번호 :
4장 예제 문제 - 시각

🍈문제 정의 :
0시0분0초부터 N시59분59초까지의 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 구하기.
입력값은 N시.

🍊풀이 시간 :
15분

🍒풀이 방법 :
h(시),m(분),s(초) = 0,0,0을 시작으로, s를 1씩 더하며 각 자리에 3이 있으면 카운팅하기.
h가 N이 되면 루프는 끝남.
s와 m은 59가 되면 다음자리(m,h)의 값이 추가됨.

*솔루션은 3중for문, 내 솔루션은 whlie문 하나라서 내 풀이가 더 빠르게 작동하는 것 같다.

'''

class Solution:
    def time(self):
        N = int(input("시간을 입력하기(시) : "))
        
        h,m,s = 0,0,0
        count = 0
        
        while h <= N :
            s +=1
            if s >= 60 :
                s = 0
                m +=1
            
            if m >= 60 :
                m = 0
                h +=1
            
            if '3' in str(h)+str(m)+str(s) :
                count +=1

        print("결과 : ",count)

test=Solution()
test.time()
        