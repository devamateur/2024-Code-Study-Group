class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]           # 현재 문자에 해당하는 노드로 갱신
        cur['END'] = ''            # 문자의 끝을 표시함으로써 문자 구분 
                                    # ex)apple, app -> {'a': {'p': {'p': {'l': {'e': {'END': {}}}}}}}, {'a': {'p': {'p':{'END':}}}}

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur:
                return False
            cur = cur[w]           # 현재 문자에 해당하는 노드로 갱신

        return 'END' in cur        # 문자 끝에 END가 있으면 단어가 검색된 것이므로 True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True