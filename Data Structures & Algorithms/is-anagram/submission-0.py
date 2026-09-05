class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
# 시간복잡도 O(n log n), 공간복잡도 O(n)