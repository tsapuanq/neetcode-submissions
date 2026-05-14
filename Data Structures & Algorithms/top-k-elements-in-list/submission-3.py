class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = dict() 
        for i in nums:
            a[i] = a.get(i, 0) + 1
        result = sorted(a, key=a.get)
        return result[::-1][:k]
        