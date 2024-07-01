'''
706. Design HashMap
https://leetcode.com/problems/design-hashmap/description/

[문제] 해시맵 디자인하기
time : 10m,, 이 풀이를 원하는 것 같지 않은데,,,
'''

class MyHashMap:
    
    def __init__(self):
        self.table = {}

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        return self.table[key] if key in self.table.keys() else -1

    def remove(self, key: int) -> None:
        if key not in self.table.keys() :return
        del self.table[key]
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)