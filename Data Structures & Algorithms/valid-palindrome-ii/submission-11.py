class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        left = 0
        right = n - 1
        count = 1
        while left < right:
            if s[left] == s[right]:
                if left == right:
                    return True
                else:
                    left += 1
                    right -= 1
            else:
                if count != 0:
                    if s[left+1] == s[right]:
                        left += 2
                        right -= 1
                        count = 0
                    elif s[left] == s[right-1]:
                        left += 1
                        right -= 2
                        count = 0
                    else:
                        return False
                else:
                    return False
        return True
