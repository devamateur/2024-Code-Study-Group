class Solution:
    # Boyer-Moore 과반수 투표 알고리즘
    # 시간복잡도: O(n), 공간복잡도: O(1)
    # https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/
    def majorityElement(self, nums: List[int]) -> int:
        count = candidate = 0

        for num in nums:
            if count == 0:  # 후보 선정 및 교체(count가 0인 경우, 후보의 수만큼 다른 숫자가 있다는 것을 의미하므로 후보 교체)
                candidate = num
            if candidate == num:     # 같은 숫자가 계속 나오면 카운트 증가
                count += 1
            else:                    # 다른 숫자는 카운트 감소
                count -= 1
        
        return candidate
    
    def majorityElement2(self, nums: List[int]) -> int:
        # 시간복잡도: O(n^2)
        for num in nums:
            if nums.count(num) > len(nums)//2:         # 카운트가 과반수보다 크면 해당 숫자 리턴
                return num