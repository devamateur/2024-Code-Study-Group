'''
🍪문제 번호 :
15장 이진탐색 - 28 : 고정점 찾기

🍈문제 정의 :
N개의 수열은 서로 다른 원소를  포함하고 있으며 오름차순으로 정렬되어 있다. 여기서 고정점을 구하기(없다면 -1)
시간복잡도 O(logN)

🍊풀이 시간 :
5분

🍒풀이 방법 :
27번 문제와 같은 풀이과정
왼족이진탐색, 오른쪽이진탐색을 통해 값 구함.


'''
class Solution :
    def run(self):
            
        # 입력
        N = int(input('N개 : '))
        components = list(map(int,input().split()))
        
        def binary_search(left,right):
            if left>right :
                return 0
            
            mid = (left+right)//2
            
            if components[mid] == mid :
                return mid

            leftsearch=binary_search(left,mid-1)
            rightsearch=binary_search(mid+1,right)
            
            return leftsearch + rightsearch
        
        result = binary_search(0,N-1)
        print("결과 : ",-1 if result==0 else result)
        return 
    
test = Solution()
test.run()