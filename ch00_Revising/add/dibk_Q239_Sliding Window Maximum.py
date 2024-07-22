'''
🍪문제 번호 :
*슬라이딩윈도우
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/description/

🍈문제 정의 :
정수 배열 nums가 있고, k사이즈 윈도우가 왼>오 방향으로 움직인다.
윈도우 크기로 움직었을때, 윈도우 사이즈 내에서 가장 큰 값을 리스트값으로 추출하기.

🍊풀이 시간 :
failed

🍒풀이 방법 :
1) k만큼 for문을 순회하여 tmp(deque)에 nums[:k]사이의 큰 값 *인덱스* 넣기
    - 결과적으로, tmp에 맨 앞은 k사이즈 안에 가장 큰 값의 인덱스가 있고, 그 뒤는 무의미
2) nums를 모두 순회하는데 for문 안에서 *현재인덱스값*과 *현재인덱스+k위치값*을 비교한다.
    - *현재인덱스값*이 tmp의 첫번째 값[0]과 같으면, k사이즈 안의 가장 큰값위치까지 왔다는 의미
    - tmp의 마지막값[-1]과 *현재인덱스+k위치값*을 비교했을 때, k사이즈위치의 값이 크면 tmp를 뒤에서 인덱스위치를 삭제해야한다.
    - 왜냐하면, tmp는 k사이즈 안에 있는 인덱스값들이고, tmp[0]이 가장 큰 값을 가지고 있는 상태, tmp[0]은 현재인덱스값이 도래했을때 사라지는 값이므로 tmp[0]위치보다 크면 tmp[0]이 되어야하고, 아니라면 두번째 큰 숫자로 입력되어야하기 때문

이 문제에서 포인트는 인덱스 위치값을 저장하는 것, while문에서 tmp의 마지막값 비교, 현재 인덱스값 비교가 핵심으로 보인다.

'''
# solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    	# 슬라이딩 윈도우의 크기가 1인 경우, 그냥 최댓값은 배열 자기 자신이나 마찬가지이다.
        if k == 1: return nums
        
        # 연산에 사용될 deque : 인덱스값 저장
        tmp = deque()
        
        # 답이 저장될 곳 : 실제 숫자, 값 저장
        result = []
        
        # 1. 첫번째 슬라이딩 윈도우를 만들고, 그 최댓값을 구해 넣는 과정
        for i in range(k):
            while tmp and nums[tmp[-1]] < nums[i]:          # tmp의 마지막값이 현재값보다 작으면, 현재값보다 클때까지 tmp에서 빼버리기
                tmp.pop()
            tmp.append(i)                                   # 그래야 tmp마지막값이 가장 최근의 큰 값으로 저장됨.(인덱스 저장)
            
        result.append(nums[tmp[0]])                         # result는 해당 값을 넣기(인덱스x)
        
        # 2. 두번째 슬라이딩 윈도우부터 계산한다.
        # left : 슬라이딩 윈도우에서 사라져야할 index의 위치 ( 왼쪽 )
        for left in range(len(nums) - k):
            # deque의 첫번째 index가 left와 일치하면 사라지는 부분이기에 제거
            if left == tmp[0]:
                tmp.popleft()
            
            # 우측에 값을 추가하기 전에 추가되는 값보다 앞의 값이 작으면 pop 한다.
            # tmp 비어있으면 멈추도록 tmp를 조건식에 넣는다.
            while tmp and nums[tmp[-1]] < nums[left+k]:
                tmp.pop()
            
            # 오른쪽 값 추가
            tmp.append(left+k)
            
            # 본 슬라이딩 윈도우의 최댓값을 append
            result.append(nums[tmp[0]])
            
        return result

# failed
# nums = [7,2,4], k =2
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tmp = deque([])
        result = []
        
        for i in range(len(nums)):

            if not tmp :
                tmp.append(nums[i])

            elif tmp[0] <= nums[i] :
                tmp.appendleft(nums[i])
            
            else:
                # tmp[0] > nums[i] :
                tmp.append(nums[i])

            if len(tmp) >= k :
                result += tmp[0],
                tmp.pop()
        
        return result


# failed
# k를 잘못이해함.
# k사이즈 안에 최대값..
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=1 : return nums
        
        tmp = deque([nums[0]])
        result = []
        
        for i in range(1,len(nums)):

            if tmp[0] <= nums[i] :
                tmp.appendleft(nums[i])
            
            else:
                # tmp[0] > nums[i] :
                tmp.append(nums[i])

            if len(tmp) >= k :
                result += tmp[0],
                tmp.pop()
        
        return result

#failed
# 시간 초과
# k = 50000
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1) :
            result +=max(nums[i:i+k]),
        
        return result