class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        def is_pal(s, left, right):
            check = True
            while left < right:
                if s[left] == s[right]:
                    left +=1
                    right -= 1
                else:
                    check = False
                    break
            return check

        while left < right:
            if s[left] == s[right]:
                if left == right:
                    return True
                else:
                    left += 1
                    right -= 1
            else:
                if s[left+1] == s[right]:
                    check = is_pal(s, left+1, right)
                    if check == True:
                        return True
                    else:
                        pass

                if s[left] == s[right - 1]:
                    check = is_pal(s, left, right-1)
                    if check == False:
                        return False
                    else:
                        return True
                else:
                    return False
        return True