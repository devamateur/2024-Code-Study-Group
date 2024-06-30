'''
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/description/

[time] failed
[문제] k사이즈 내에서 최대값을 찾아 리턴하기.
[풀이방식] :
- 첫번째 답지와 같은 풀이었지만, 타임아웃, 두번째 답지도 타임아웃
    - for문 시간복잡도(O(N)), max시간복잡도(O(k)) >> O(NK)
- 큐를 이용한 최적화 풀이법
 - window(deque)에 해당 윈도우 내 최대값의 인덱스를 저장하기
 - window의 앞자리는 무조건 최대값만 넣어두고, 새로운 값이 추가될 때, window앞자리와 비교하여 값이 작으면 패스, 크면 window를 재정렬하는 방법


'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        nums = [1,3,-1,-3,5,3,6,7], k = 3
               [3]
               
        output : 3, 3, 5, 5, 6, 7

        '''
        if k==1 : return nums
        
        window_idx = collections.deque()
        result = []

        for cur_idx in range(len(nums)):
            
            while window_idx and nums[cur_idx] > nums[window_idx[-1]]:        # window_idx의 마지막 인덱스의 값이 nums[cur_idx]값보다 작으면, 해당 인덱스 값 빼주기
                window_idx.pop()
            window_idx.append(cur_idx)                                        # window_idx : 인덱스 값 저장
            
            if cur_idx - k == window_idx[0]:                                  # 현재 인덱스(cur_idx) - k의 값이 window_idx[0]의 인덱스값과 같으면(윈도우 사이즈를 넘어버리면) 인덱스 값 빼주기.
                window_idx.popleft()                                          # if. window_idx :: [0,2]
                                                                              # cur_idx(3) - k(3) = 0이라면, 다음 for문에서는 윈도우 사이즈를 넘어가므로 0인덱스를 빼준다.
                                                                              
            if cur_idx >= k-1:                                                # 현재 인덱스(cur_idx)가 윈도우 사이즈 이상일때부터 result에 저장하기.
                result.append(nums[window_idx[0]])                            # k-1 :: 2, 2이상부터는 항상 window_idx[0]의 값을 result에 저장함.
                
        return result

# Time Limit Exceeded
# 37 / 51 testcases passed
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums : return nums

        result = []

        for idx in range(len(nums)-k+1):
            result.append(max(nums[idx:idx+k]))
        
        return result