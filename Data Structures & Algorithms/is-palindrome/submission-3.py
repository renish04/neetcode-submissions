class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        n = len(s)

        left = 0
        right = n-1

        while left < right:
            if s[left].isalnum() is True:
                if s[right].isalnum() is True: 
                    if s[left].lower() == s[right].lower():
                        left += 1
                        right -= 1

                    else:
                        return False
                elif s[right].isalnum() is False:
                    right -= 1
            elif s[left].isalnum() is False:
                    left += 1
            
             
        return True