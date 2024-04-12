class MyHashMap:
    
    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map.get(key) is not None:            # if self.map.get(key)으로 하면 오답이 되는데 왜인지 이유를 모르겠음..
            return self.map.get(key)
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)