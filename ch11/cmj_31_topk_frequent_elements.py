import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}         # {원소: 등장횟수} 저장

        for n in nums:
            if n not in my_dict:
                my_dict[n] = 1
            else:
                my_dict[n] += 1
        
        result = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))       # 등장횟수를 기준으로 내림차순 정렬
        
        return list(result.keys())[:k]         # k개 리턴

    def oneLine(self, nums: List[int], k: int) -> List[int]:
        # collections.Counter(nums).most_common(k): 가장 흔한 k개 원소와 등장 횟수를 튜플의 리스트 형태로 리턴 ex) [1, 1, 3, 4, 5], k=2 -> [(1, 2), (3, 1)]
        # zip(*): unpacking. 튜플의 각 첫 번째, 두 번째, ... n번째 요소를 가져와 튜플의 리스트 형태로 만듦 ex) [(1, 2), (3, 1)] -> [(1, 3), (2, 1)]
        # list(): 언패킹한 튜플의 0번째 원소를 가져옴
        return list(zip(*collections.Counter(nums).most_common(k)))[0]