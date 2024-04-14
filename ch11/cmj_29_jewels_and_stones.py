from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_map = defaultdict(int)      # defaultdict 사용 

        for ch in stones:
            if ch in jewels:
                jewel_map[ch] += 1

        result = sum(jewel_map.values()) if sum(jewel_map.values()) != 0 else 0
        return result