'''
🍪문제 번호 :
6장 실전 문제 - 성적이 낮은 순서로 학생 출력하기

🍈문제 정의 :
N명의 학생 정보를 통해 성적순으로 출력하기(오름차순, (1<=N<=100,000))

🍊풀이 시간 :
10분

🍒풀이 방법 :
*https://www.nossi.dev/cote/timecomplexity

10만데이터로 O(N^2)은 불가능, O(nlogN), O(N), O(logN)
sort함수는 O(nlogN)이므로 가능
   
'''

class Solution :
    
    def outputTotheScore(self):
        # 입력
        N =int(input("입력할 학생 수 : "))
        info = {}

        for _ in range(N):
            student,score = map(str,input().split())
            info[int(score)] = student
        
        result = [name for (score,name) in sorted(info.items())]
        
        print("결과 : ",result)
                                                 
        
        return 
test = Solution()
test.outputTotheScore()