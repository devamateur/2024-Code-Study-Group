'''
🍪문제 번호 :
6장 실전 문제 - 두 배열의 원소 교체

🍈문제 정의 :
두 배열(A,B)은 N개의 원소로 구성되어 있으며, 최대 K번 교체 연산 수행을 통해 A배열의 원소합이 최대가 되도록 구하기.

🍊풀이 시간 :
15분

🍒풀이 방법 :
A배열의 가장 작은 값을 k개 뽑고, B배열에서는 가장 큰 값을 K개 뽑는다.
A의 요소와 B의 요소를 비교하는데, A의 요소가 B 요소보다 크면 A의 다음 교체 요소와 비교 연산을 수행하며 바꾸는 작업을 실시한다.

   
'''

class Solution :
    
    def ChangeThElements(self):
        # 입력
        N,K = map(int,input("입력할 배열의 요소와 K : ").split())
        
        a = list(map(int,input().split()))
        a.sort() 
        a_k = a[:K]
        
        b = list(map(int,input().split()))
        b.sort() 
        b_k = b[-K:]
        
        tmp = []
        i = 0
        for c in a_k[::-1]:
            if c < b_k[i] :
                tmp.append(b_k[i])
            else :
                tmp.append(c)
            
            i+=1

        result = a[K:] + tmp
        print("결과 : ",sum(result))
                                                 
        
        return 
test = Solution()
test.ChangeThElements()