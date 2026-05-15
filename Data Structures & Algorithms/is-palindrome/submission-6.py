class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.strip('?!@#$%^&*,\'').lower()#.replace(' ', '')
        b = []
        for i in s:
            i = i.lower()
            a = ord(i)
            if a in range(97, 123):
                b.append(i)
            elif a in range(48, 58):
                b.append(i)
        return b == b[::-1]