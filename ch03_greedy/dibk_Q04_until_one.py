'''
문제 번호 :
3장 실전 문제 4 : 1이 될 때까지

문제 정의 :
N에서 1빼기, N을 K로 나누기
두 과정 중 하나를 반복적으로 수행하여 어떤 수 N이 1이 될 때까지 연산을 수행한다.
최소 연산 횟수를 구하기.

풀이 시간 : 
9분

풀이 방법 :
우선 N값을 K로 나누고, 나누기가 안되면 -1
위 풀이 순으로 값을 계산하기

'''
class Solution():
    
    def until_one(self) -> None :
        N,K = map(int,input("N과 K를 입력하기(공백기준): ").split())
        
        result = 0
        while N > 1 :
            
            # division
            if N%K == 0 :
                N = N//K
                result +=1
                continue
            
            # minus
            N -=1
            result +=1
        
        print()
        print("최소 연산 횟수 : ",result)
    
        return
    
test = Solution()
test.until_one()