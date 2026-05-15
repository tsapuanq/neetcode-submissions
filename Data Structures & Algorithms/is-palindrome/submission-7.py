class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = []
        for char in s:

            char = char.lower()
            unicode = ord(char)

            if unicode in range(97, 123):
                result.append(char)

            elif unicode in range(48, 58):
                result.append(char)
                
        return result == result[::-1]