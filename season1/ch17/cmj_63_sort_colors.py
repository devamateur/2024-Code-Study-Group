import collections

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counting = collections.defaultdict(int)

        for i, num in enumerate(nums):
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
                    
        return nums