'''
🍪문제 번호 :
7장 실전문제 - 부품 찾기

🍈문제 정의 :
가게에 N개의 부품이 있으며, 손님은 M개의 부품을 찾고 있다.
1<= N <= 1,000,000(백만)
1<= M <= 100,000(십만)

🍊풀이 시간 :
25분

🍒풀이 방법 :
먼저 가게의 부품을 정렬하고(sort함수 사용시, O(NlogN))
손님의 물건을 이진 탐색으로 찾기(이진 탐색 시, O(MlogN))
최종 시간 복잡도는 NlogN + MlogN = (N+M)logN

'''

class Solution :
    
    def finding(self):
        # 입력
        N = int(input("N : "))
        store = list(map(int,input().split()))
        store.sort()                            # 가게 부품 정렬
        
        M= int(input("M : "))
        customer = list(map(int,input().split()))
        
        def run(target,start,end):
            
            while start <= end :
                mid = (start+end)//2
                
                if store[mid] == target :
                    return 'yes'
                elif store[mid] > target :
                    end = mid-1
                else :
                    # store[mid] < target 
                    start = mid +1
            
            return 'no'
        
        result = []
        for part in customer :
            result +=run(part,0,N-1),
        
        print("결과 : ",' '.join(result))
                                                 
        
        return 
test = Solution()
test.finding()