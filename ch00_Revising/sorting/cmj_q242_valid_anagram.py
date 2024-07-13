class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)            # 정렬한 두 문자열이 같으면 애너그램