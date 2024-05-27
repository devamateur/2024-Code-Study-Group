import collections

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 두 배열의 {숫자: 개수} 저장
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)

        for num in nums1:
            count1[num] += 1
        for num in nums2:
            count2[num] += 1

        result = set()        # 결과 셋

        # 숫자가 두 딕셔너리에 모두 있으면
        for num in count1:
            if num in count2:
                result.add(num)
        
        return list(result)

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = set()

        # 투포인터
        # 각각 nums1, nus2의 인덱스
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:  # 같은 숫자가 있는 경우, 결과에 추가하고 두 배열 모두 오른쪽으로 이동
                result.add(nums1[i])
                i += 1
                j += 1
        
        return list(result)