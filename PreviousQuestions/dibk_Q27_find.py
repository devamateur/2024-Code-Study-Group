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


# bisect 라이브러리
'''
원소들이 **정렬된** 리스트에서 특정 원소를 찾을 때 효과적

(1)  bisect_left(list, data): 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지).

(2)  bisect_right(list, data): 리스트에 데이터를 삽입할 가장 오른쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지).

from bisect import bisect_left, bisect_right

# [left_v, right_v] 범위 내에 있는 원소 개수 출력 함수
def cnt_within_range (arr, left_v, right_v):
    # 맨 좌측 인덱스
    left_idx = bisect_left(arr, left_v)
    # 맨 우측 인덱스
    right_idx = bisect_right(arr, right_v)
    return right_idx - left_idx

# 리스트 생성
arr = [5, 6, 7, 7, 7, 7, 8, 8, 9, 10]

# 값이 9인 원소 개수 출력
print(cnt_within_range(arr, 9, 9)) # 1
# [4, 7] 범위 내에 있는 원소 개수 출력
print(cnt_within_range(arr, 4, 7)) # 6


'''