class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 딕셔너리에 {정렬한 단어: 애너그램} 형태로 저장
        # 이렇게 하면, value를 가져오는 게 같은 애너그램들을 가져오는 것임
        word_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))    # sorted는 리스트를 반환하므로 string으로 변환
            if sorted_word not in word_dict:
                word_dict[sorted_word] = [word]
            else:
                word_dict[sorted_word].append(word)

        return word_dict.values()