import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # word_list = [word for word in re.split('[^a-zA-Z]',paragraph.lower()) if word not in banned]
        word_list = [word for word in re.sub('[^a-zA-Z]'," ",paragraph.lower()).split() if word not in banned]
        dict_word = {}
        
        for word in word_list :
            if word in dict_word.keys() :
                dict_word[word]+=1
            else :
                dict_word[word]=1
        
        return max(dict_word,key=dict_word.get)
    

import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        '''
        라이브러리 사용
        '''
        
        # [^\w] == [\W]
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]