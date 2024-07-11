'''
🍪문제 번호 :
6장 실전 문제 - from top to bottom

🍈문제 정의 :
입력된 수를 내림차순으로 정렬하기.(1<=N<=500)

🍊풀이 시간 :
5분

🍒풀이 방법 :
sort함수 사용.
입력값 최대가 500이라서 sort시간복잡도로도 풀이가 가능하다고 생각함.
    
'''

class Solution :
    
    def formToptoDown(self):
        # 입력
        N =int(input("입력할 숫자 갯수 : "))
        nums = []

        # 1.
        for _ in range(N):
            nums +=int(input())
        nums.sort(reverse = True)
        
        # 2.
        # for _ in range(N):
        #     num =int(input())
            
        #     for i,n in enumerate(nums) :
        #         if num < n :
        #             nums = nums[:i] + [num] + nums[i:]
        #             break
        #     else :
        #         nums += num,
            
        
        print("결과 : ",nums) 
        return 
    
test = Solution()
test.formToptoDown()