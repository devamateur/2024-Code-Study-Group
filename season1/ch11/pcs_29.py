class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        count = 0
        for i in stones:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for char in jewels:
            if char in dic:
                count += dic[char]

        return count        