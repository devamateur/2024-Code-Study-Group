class Solution:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = 0  # 각각 nums1과 nums2의 인덱스스
        result = []

        # 투포인터
        while i<len(nums1) and j<len(nums2):
            if  nums1[i] not in result and nums1[i] == nums2[j]:      # 두 배열에 모두 있는 원소면 결과에 추가
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:        # nums1의 값이 작으면 i 인덱스 증가
                i += 1
            else:                  # nums2의 값이 작으면 j 인덱스 증가가
                j += 1
        return result
    
    # set 이용
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)       # set1.intersation(set2)