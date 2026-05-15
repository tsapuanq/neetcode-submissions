class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = []
        for char in s:

            char = char.lower()
            code = ord(char)

            if (97 <= code <= 122) or (48 <= code <= 57):
                result.append(char)
                
        return result == result[::-1]