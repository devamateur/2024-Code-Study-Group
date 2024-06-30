class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        IDEA
        - strs변수의 문자열을 사전순으로 정렬하여 key값으로 설정
        - 단점) Question의 Constraints "" 0 <= strs[i].length <= 100 "" 이라서 가능한 방법론
        '''
        anagrams_dict = {}

        for s in strs :
            # list_s = list(s)
            # list_s.sort()
            # key_ =''.join(list_s)
            
            key_ = ''.join(sorted(s))

            if key_ in anagrams_dict.keys():
                anagrams_dict[key_].append(s)
            else :
                # dictionary의 값을 list()로 정의할 때 주의
                anagrams_dict[key_] = [s]
        
        return [strs for strs in anagrams_dict.values()]
        # return list(anagrams_dict.values())