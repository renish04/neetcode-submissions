class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() == False:
                left += 1

            elif s[right].isalnum() == False:
                right -= 1

            else:
                if s[left].lower() == s[right].lower():
                    right -= 1
                    left += 1
                else:
                    return False
        return True
