class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = dict()
        for i in nums:
            a[i] = a.get(i, 0) + 1
            if a[i] > 1:
                return True
        return False