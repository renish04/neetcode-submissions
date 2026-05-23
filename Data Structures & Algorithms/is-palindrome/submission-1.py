class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        s = s.lower()
        print(s)
        n = len(s)

        left = 0
        right = n-1

        while left < right:
            if not (48 <= ord(s[left]) <= 57 or  65 <= ord(s[left]) <= 90 or 97 <= ord(s[left]) <= 122):
                left += 1
            if not (48 <= ord(s[right]) <= 57 or  65 <= ord(s[right]) <= 90 or 97 <= ord(s[right]) <= 122):
                right -= 1
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True