import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_dict = {}
        most_frequent = ""

        new_para = paragraph.split()

        for word in new_para:
            word = re.sub("[!?\',;.\s]", "", word)         # 특수문자 제거
            lower_case = word.lower()

            if lower_case not in word_dict:
                word_dict[lower_case] = 1
            else:
                word_dict[lower_case] += 1
        
        # 빈도수로 내림차순 정렬
        word_dict = dict(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))

        for key in word_dict.keys():
            if key in banned:
                continue
            else:  # 금지어가 아닌 단어 중 빈도가 가장 높은 단어
                most_frequent = key     
                break

        return most_frequent
    
    # 이 경우 아래 테스트 케이스 1개가 통과되지 않았음
    # Input: "a, a, a, a, b,b,b,c, c" ["a"]
    # Output: "bbbc"
    # Expected: "b"