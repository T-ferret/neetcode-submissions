class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
# 시간 복잡도 O(n), 공간 복잡도 O(n)