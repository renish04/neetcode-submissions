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
                    if s[left+1:right] == s[right:left:-1]:
                        print("1", s[left+1:])
                        print("2", s[right::-1])
                        left += 2
                        right -= 1
                        count = 0
                    elif s[left:right] == s[right-1:left:-1]:
                        print(s[left:])
                        print(s[::right-1])
                        left += 1
                        right -= 2
                        count = 0
                    else:
                        return False
                else:
                    return False
        return True
