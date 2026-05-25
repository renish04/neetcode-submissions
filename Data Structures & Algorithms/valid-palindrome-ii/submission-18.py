class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_pal(left, right):
            while left < right :
                if s[left] == s[right]:
                    left +=1 
                    right -= 1
                else:
                    return False
            return True
            
        while left < right:
            if s[left] != s[right]:
                if is_pal(left+1, right) == False:
                    return is_pal(left, right-1)
                else:
                    return True
            else:
                left += 1
                right -= 1

        return True