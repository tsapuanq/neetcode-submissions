class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = dict()
        for i in strs:
            b = ''.join(sorted(i))
            if b not in a:
                a[b] = [i] 
            elif b in a:
                a[b] += [i]
        
        return([*a.values()])