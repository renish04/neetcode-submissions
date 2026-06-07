class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i < len(s)//2:
            if s[i] == "{" and s[j] == "}":
                i += 1
                j -= 1
            elif s[i] == "(" and s[j] == ")":
                i += 1
                j -= 1
            elif s[i] == "[" and s[j] == "]":
                i += 1
                j -= 1
            else:
                return False

        return True
