'''
🍪문제 번호 :
15장 이진탐색 - 27 : 정렬된 배열에서 특정 수의 개수 구하기

🍈문제 정의 :
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있고, 이때 수열에서 x가 등장하는 횟수를 구하기.
시간복잡도 O(logN)

🍊풀이 시간 :
35분

🍒풀이 방법 :
이진탐색(재귀)
- 이진탐색 함수를 정의할 때, left가 right보다 커지는 순간이 루프가 끝나는 조건으로 정의함.
- 값을 확인하는 인덱스는 무조건 mid인덱스로 계산하기(count+1)
- 왼쪽이진탐색 + 오른쪽이진탐색 + count로 재귀하여 값 구하기.

'''
class Solution :
    def run(self):
            
        # 입력
        N,x = map(int,input('N개, x값 : ').split())
        components = list(map(int,input().split()))
        
        def binary_search(left,right,target,count):
            if left>right :
                return 0
            
            mid = (left+right)//2
            
            if components[mid] == target :
                count +=1

            leftsearch=binary_search(left,mid-1,target,0)           # 매개변수의 마지막(count)부분을 0으로 정의해야 중복으로 재귀값 갖지 않음
            rightsearch=binary_search(mid+1,right,target,0)
            
            return leftsearch + rightsearch + count
        
        result = binary_search(0,N-1,x,0)
        print("결과 : ",-1 if result==0 else result)
        return 
    
test = Solution()
test.run()