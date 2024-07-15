import collections

class Solution:
    # 직접 정렬 (버블 정렬 형태)
    def sortColors1(self, nums: List[int]) -> None:
        
        idx = 1

        while idx < len(nums):
            while idx>0 and nums[idx-1] > nums[idx]:
                nums[idx-1], nums[idx] = nums[idx], nums[idx-1]          # 값 교환
                idx -= 1                            # 앞뒤 값이 모두 2나 1일 경우 제대로 정렬하기 위해 인덱스 감소

            idx += 1
    
    # 딕셔너리 이용
    def sortColors2(self, nums: List[int]) -> None:
        counting = collections.defaultdict(int)

        for _, num in enumerate(nums):
            counting[num] += 1      # {숫자: 개수} 저장

        counting = dict(sorted(counting.items(), key=lambda x:x[0]))

        idx = 0
        colors = 0
        while idx < len(nums):
            # 해당 컬러가 없으면 다음 컬러로
            if colors not in counting:
                colors += 1
                continue

            # 컬러가 있으면
            if colors in counting:
                nums[idx] = colors       # 해당 컬러로 값 갱신
                counting[colors] -= 1    # 개수 감소
                if counting[colors] == 0:       # 현재 컬러를 다 사용하면 다음 컬러로
                    colors += 1
            idx += 1 
            if colors > 2:
                break