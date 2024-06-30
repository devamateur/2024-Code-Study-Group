'''
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/description/

[time] failed
[문제] 
[풀이방식]
- 딕셔너리의 딕셔너리 생성하기
- 해당 단어 입력이 끝났을 때, 'word_bool' : True 로 단어가 존재한다는 것을 표기
- 
'''

class Trie:
    
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        
        for w in word:              # # {'a': {'p': {'p': {'l': {'e': {'word_bool': True}}}}}}
            if w not in node:
                node[w] = {}
            node = node[w]
     
        node['word_bool'] = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node:
                return False
            else:
                node = node[w]

        if 'word_bool' in node:
            return True
        else:
            return False    

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for p in prefix:
            if p not in node:
                return False
            else:
                node = node[p]
        return True